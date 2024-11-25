from django.urls import path
from . import views
from .views import CreatePostView, PostEditView, PostDeleteView, PostDetailView, school_detail, add_school, school_list, \
    SchoolSearchAPIView

urlpatterns = [
    path('new-post/', CreatePostView.as_view(), name='new_post'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/edit/', PostEditView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('schools_list/', school_list, name='school_list'),
    path('school/<int:school_id>/', school_detail, name='school_detail'),
    path('add_school/', add_school, name='add_school'),
    path('api/schools/search/', SchoolSearchAPIView.as_view(), name='school_search_api'),
]
