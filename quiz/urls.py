from django.urls import path
from quiz.views import QuizView, CreateQuizView, QuizSearchAPIView

urlpatterns = [
    path('quiz_home/', QuizView.as_view(), name='quiz_home'),
    path('quiz/create/', CreateQuizView.as_view(), name='create_quiz'),
    path("api/quiz/search/", QuizSearchAPIView.as_view(), name="search_quizzes"),

]
