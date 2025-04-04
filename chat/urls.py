
from django.urls import path
from . import views
urlpatterns = [
    path('', views.messages_page, name='chat'),
    path('chat/<int:thread_id>/', views.chat_room, name='chat_room'),
    path('start_chat/<int:user_id>/', views.start_chat, name='start_chat'),

    path('chat/api/messages/<int:thread_id>/', views.get_chat_messages, name='get_chat_messages'),
]
#