from django.urls import path

from posts.views import DashBoardListView
from .views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('dashboard/', DashBoardListView.as_view(), name='dashboard'),
]
