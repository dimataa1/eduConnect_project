from django.urls import path
from . import views
from .views import CreatePostView, PostEditView, PostDeleteView, PostDetailView

urlpatterns = [
    path('new-post/', CreatePostView.as_view(), name='new_post'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/edit/', PostEditView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),

]
