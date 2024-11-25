from django.shortcuts import render
from django.urls import path
from .views import register, LoginView, LogoutView

urlpatterns = [
    path('register/', register, name='register'),
    path('pending-approval/', lambda request: render(request, 'accounts_structure/pending_approval.html'), name='pending-approval'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

]

