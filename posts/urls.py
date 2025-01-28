from django.urls import path
from . import views
from .views import CreatePostView, PostEditView, PostDeleteView, PostDetailView, school_detail, add_school, school_list, \
    post_list, vote_comment, TourListView, TourDetailView, TourEditView, TourDeleteView

urlpatterns = [
    path('new-post/', CreatePostView.as_view(), name='new_post'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/edit/', PostEditView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),

    path('schools_list/', school_list, name='school_list'),
    path('school/<int:school_id>/', school_detail, name='school_detail'),
    path('add_school/', add_school, name='add_school'),

    path('post_list/', post_list, name='post_list'),
    path('post/<int:post_id>/vote/<int:comment_id>/<str:vote_action>/', vote_comment, name='vote_comment'),

    path('create_tour/', views.CreateTourView.as_view(), name='create_tour'),
    path('tours/', TourListView.as_view(), name='tour_list'),
    path('tour/<int:pk>/', TourDetailView.as_view(), name='tour_detail'),
    path('tour/<int:pk>/edit/', TourEditView.as_view(), name='tour_edit'),
    path('tour/<int:pk>/delete/', TourDeleteView.as_view(), name='tour_delete'),
]
