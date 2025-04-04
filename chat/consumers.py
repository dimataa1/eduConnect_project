import json
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model
from chat.models import Thread, ChatMessage

User = get_user_model()

class ChatConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        self.thread_id = self.scope['url_route']['kwargs']['thread_id']
        self.room_name = f'chat_{self.thread_id}'

        await self.channel_layer.group_add(
            self.room_name,
            self.channel_name
        )
        await self.send({
            'type': 'websocket.accept'
        })
        print(f"[CONNECTED] {self.channel_name} joined room {self.room_name}")

    async def websocket_receive(self, event):
        print('[RECEIVED]', event)

        try:
            data = json.loads(event['text'])
        except json.JSONDecodeError:
            print("Error decoding JSON")
            return

        message = data.get('message')
        sent_by_id = data.get('sent_by')
        send_to_id = data.get('send_to')
        thread_id = data.get('thread_id')

        if not message:
            print('Error: Empty message')
            return

        # Fetch objects from DB
        sent_by_user = await self.get_user_object(sent_by_id)
        send_to_user = await self.get_user_object(send_to_id)
        thread_obj = await self.get_thread(thread_id)

        if not all([sent_by_user, send_to_user, thread_obj]):
            print("Error: Missing user or thread")
            return

        # Save the message
        await self.create_chat_message(thread_obj, sent_by_user, message)

        response = {
            'message': message,
            'sent_by': sent_by_user.id,
            'send_to': send_to_user.id,
            'thread_id': thread_id
        }

        # Broadcast to both users in the same thread room
        await self.channel_layer.group_send(
            self.room_name,
            {
                'type': 'chat_message',
                'text': json.dumps(response)
            }
        )

    async def chat_message(self, event):
        await self.send({
            'type': 'websocket.send',
            'text': event['text']
        })

    async def websocket_disconnect(self, event):
        print(f"[DISCONNECTED] {self.channel_name} left room {self.room_name}")
        await self.channel_layer.group_discard(
            self.room_name,
            self.channel_name
        )

    # ===== DB Helpers =====
    @database_sync_to_async
    def get_user_object(self, user_id):
        return User.objects.filter(id=user_id).first()

    @database_sync_to_async
    def get_thread(self, thread_id):
        return Thread.objects.filter(id=thread_id).first()

    @database_sync_to_async
    def create_chat_message(self, thread, user, msg):
        return ChatMessage.objects.create(thread=thread, user=user, message=msg)
