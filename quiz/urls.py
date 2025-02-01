from django.urls import path
from quiz.views import (
    QuizView,
    CreateQuizView,
    QuizSearchAPIView,
    QuizDetailView, QuizAPIView, textChatBot,
)

urlpatterns = [
    path('quiz/create/', CreateQuizView.as_view(), name='create_quiz'),
    path('api/quiz/search/', QuizSearchAPIView.as_view(), name='search_quizzes'),
    path('quiz/<int:pk>/', QuizDetailView.as_view(), name='quiz_detail'),
    path('quiz_home/', QuizView.as_view(), name='quiz_home'),
    path('api/quiz/<int:quiz_id>/', QuizAPIView.as_view(), name='quiz_api'),
    path('quiz/chat_text_response', textChatBot, name='chat_text_response'),
]
