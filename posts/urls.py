from django.urls import path
from . import views
from .views import CreatePostView

urlpatterns = [
    path('new-post/', CreatePostView.as_view(), name='new_post'),
]
