
from django.shortcuts import render
from django.urls import path

from .forms import profile_details_view, profile_update_view
from .views import register, LoginView, LogoutView, delete_profile_picture, ProfileDeleteView, change_password

urlpatterns = [
    path('register/', register, name='register'),
    path('pending-approval/', lambda request: render(request, 'accounts_structure/pending_approval.html'), name='pending-approval'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/<str:username>/', profile_details_view, name='profile_details'),
    path('profile/update/', profile_update_view, name='profile_update'),
    path('profile/picture/delete/', delete_profile_picture, name='delete_profile_picture'),
    path('profile/delete/', ProfileDeleteView.as_view(), name='delete_profile'),
    path('profile/change-password/', change_password, name='change_password'),

]
