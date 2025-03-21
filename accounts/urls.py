
from django.shortcuts import render
from django.urls import path

from .forms import profile_details_view, profile_update_view, change_password_view
from .views import register, LoginView, LogoutView, delete_profile_picture, delete_profile

urlpatterns = [
    path('register/', register, name='register'),
    path('pending-approval/', lambda request: render(request, 'accounts_structure/pending_approval.html'), name='pending-approval'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/<str:username>/', profile_details_view, name='profile_details'),
    path('profile/<str:username>/update/', profile_update_view, name='profile_update'),
    path('profile/<str:username>/picture/delete/', delete_profile_picture, name='delete_profile_picture'),
    path('profile/<str:username>/delete/', delete_profile, name='delete_profile'),
    path('profile/<str:username>/change-password/', change_password_view, name='change_password'),

]
