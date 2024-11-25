from django.urls import path

from posts.views import DashBoardListView
from .views import HomeView, PostSearchAPIView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('dashboard/', DashBoardListView.as_view(), name='dashboard'),
    path('api/search/', PostSearchAPIView.as_view(), name='post_search_api'),
]
