from django.db import models
from django.conf import settings

class Quiz(models.Model):
    title = models.CharField(
        max_length=255
    )
    description = models.TextField()

    subject = models.CharField(
        max_length=255
    )
    grade = models.CharField(
        max_length=255
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='quizzes',
    )

    def __str__(self):
        return self.title


class Question(models.Model):
    quiz = models.ForeignKey(
        Quiz,
        related_name='questions',
        on_delete=models.CASCADE
    )

    text = models.TextField()

    question_type = models.CharField(
        max_length=50,
        choices=[
            ('MCQ', 'Multiple Choice'),
            ('TF', 'True/False'),
            ('SA', 'Short Answer')
        ]
    )

    class Meta:
        unique_together = ('quiz', 'text')

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(
        Question,
        related_name='answers',
        on_delete=models.CASCADE
    )

    text = models.TextField()

    is_correct = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.text
