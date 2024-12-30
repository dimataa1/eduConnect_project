from django.urls import path
from quiz.views import QuizView

urlpatterns = [
    path('quiz_home/', QuizView.as_view(), name='quiz_home'),
]
