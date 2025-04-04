import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import ChatMessage, Thread
from django.contrib.auth import get_user_model

User = get_user_model()

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.thread_id = self.scope['url_route']['kwargs']['thread_id']
        self.thread = await database_sync_to_async(Thread.objects.get)(id=self.thread_id)

        # Check if the user is part of the thread
        if self.scope['user'] in [self.thread.first_person, self.thread.second_person]:
            self.room_name = f"chat_{self.thread_id}"
            self.room_group_name = f"chat_{self.thread_id}"

            # Join the chat group
            await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
            )

            await self.accept()

    async def disconnect(self, close_code):
        # Leave the chat group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        sent_by = text_data_json['sent_by']
        thread_id = text_data_json['thread_id']
        send_to = text_data_json['send_to']

        # Save the message to the database
        user = await database_sync_to_async(User.objects.get)(id=sent_by)
        thread = await database_sync_to_async(Thread.objects.get)(id=thread_id)

        chat_message = await database_sync_to_async(ChatMessage.objects.create)(
            thread=thread, user=user, message=message
        )

        # Send the message to the group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sent_by': sent_by,
                'timestamp': chat_message.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
            }
        )

    # Receive message from chat group
    async def chat_message(self, event):
        message = event['message']
        sent_by = event['sent_by']
        timestamp = event['timestamp']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'sent_by': sent_by,
            'timestamp': timestamp,
        }))
