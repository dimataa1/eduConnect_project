
from django.urls import path
from . import consumers


websocket_urlpatterns = [
    path('chat_structure/', consumers.ChatConsumer.as_asgi()),
]
#