from django.urls import path
from chat.views import ChatRoomView, MessagesView

urlpatterns = [
	path('chats/<str:userId>/', ChatRoomView.as_view(), name='chatRoom'),
	path('chats/<str:roomId>/messages/', MessagesView.as_view(), name='messageList'),
	path('users/<int:userId>/chats/', ChatRoomView.as_view(), name='chatRoomList'),
]
