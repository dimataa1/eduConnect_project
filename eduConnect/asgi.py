"""
ASGI config for eduConnect_project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application

# For Django Channels or WebSocket support, you would add the channels layers and protocols routing here
# from channels.routing import ProtocolTypeRouter, URLRouter
# from channels.auth import AuthMiddlewareStack

# Set the default settings module for the 'asgi' application.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eduConnect_project.settings')

# Uncomment the following if using Django Channels with WebSockets:
# application = ProtocolTypeRouter({
#     "http": get_asgi_application(),
#     "websocket": AuthMiddlewareStack(
#         URLRouter(
#             # Define your WebSocket URL routing here
#         )
#     ),
# })

# For most standard setups without Django Channels:
application = get_asgi_application()
