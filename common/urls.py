from django.urls import path

from posts.views import DashBoardListView
from .views import HomeView, PostSearchAPIView, SchoolSearchAPIView, AcademicCalendarView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('dashboard/', DashBoardListView.as_view(), name='dashboard'),
    path('api/search/', PostSearchAPIView.as_view(), name='post_search_api'),
    path('api/schools/search/', SchoolSearchAPIView.as_view(), name='school_search_api'),
    path('calendar/', AcademicCalendarView.as_view(), name='academic_calendar'),

]
