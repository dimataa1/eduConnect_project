# consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import ChatMessage, Thread
from django.contrib.auth import get_user_model

User = get_user_model()


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.thread_id = self.scope['url_route']['kwargs']['thread_id']
        self.user = self.scope['user']
        self.room_group_name = f'chat_{self.thread_id}'

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        # Accept WebSocket connection
        await self.accept()

        # Send previous messages to the WebSocket client
        thread = await database_sync_to_async(Thread.objects.get)(id=self.thread_id)
        messages = await database_sync_to_async(ChatMessage.objects.filter)(thread=thread)
        messages_data = [{
            'message': msg.message,
            'sent_by': msg.user.id,
            'timestamp': msg.timestamp.strftime('%Y-%m-%d %H:%M:%S')
        } for msg in messages]

        await self.send(text_data=json.dumps({
            'messages': messages_data
        }))

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        sent_by = data['sent_by']
        thread_id = data['thread_id']
        send_to = data['send_to']

        # Save the message to the database
        thread = await database_sync_to_async(Thread.objects.get)(id=thread_id)
        user = await database_sync_to_async(User.objects.get)(id=sent_by)
        chat_message = await database_sync_to_async(ChatMessage.objects.create)(
            message=message, thread=thread, user=user
        )

        # Broadcast the message to the group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sent_by': sent_by,
                'timestamp': chat_message.timestamp.strftime('%Y-%m-%d %H:%M:%S')
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        sent_by = event['sent_by']
        timestamp = event['timestamp']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'sent_by': sent_by,
            'timestamp': timestamp
        }))
