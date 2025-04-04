import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from chat import consumers  # Adjust this to your chat app

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'educonnect.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path("ws/chat/<int:thread_id>/", consumers.ChatConsumer.as_asgi()),
        ])
    ),
})
