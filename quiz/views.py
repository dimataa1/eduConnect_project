import json

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import QuizSearchForm, FileUploadForm, QuizForm, QuestionForm, AnswerForm
from .models import Quiz, Question
from django.shortcuts import render, redirect
from .forms import QuestionFormSet, AnswerFormSet
from .models import Quiz, Question, Answer
from django.contrib.auth.decorators import login_required


class QuizView(View):
    def get(self, request, *args, **kwargs):
        search_form = QuizSearchForm()
        file_form = FileUploadForm()

        if request.user.is_authenticated:
            context = {
                'username': request.user.username,
                'search_form': search_form,
                'file_form': file_form,
                'quizzes': Quiz.objects.all(),
            }
            return render(request, 'quiz_structure/quiz_landing_page.html', context)

    def post(self, request, *args, **kwargs):
        if 'search' in request.POST:
            search_form = QuizSearchForm(request.POST)
            if search_form.is_valid():
                subject = search_form.cleaned_data.get('subject')
                grade = search_form.cleaned_data.get('grade')

                quizzes = Quiz.objects.filter(
                    subject__icontains=subject,
                    grade=grade
                )
                return render(request, 'quiz_structure/quiz_landing_page.html', {
                    'username': request.user.username,
                    'search_form': search_form,
                    'file_form': FileUploadForm(),
                    'quizzes': quizzes,
                })

        elif 'upload' in request.POST:
            file_form = FileUploadForm(request.POST, request.FILES)
            if file_form.is_valid():
                uploaded_file = file_form.cleaned_data['file']
                file_data = uploaded_file.read().decode('utf-8')
                self.import_quiz_data(file_data)
                return redirect('quiz-page')

        return render(request, 'quiz_structure/quiz_landing_page.html', {
            'username': request.user.username,
            'search_form': QuizSearchForm(),
            'file_form': FileUploadForm(),
            'quizzes': Quiz.objects.all(),
        })

    def import_quiz_data(self, file_data):
        data = json.loads(file_data)

        for quiz_data in data.get("quizzes", []):
            quiz = Quiz.objects.create(
                title=quiz_data["quiz_title"],
                subject=quiz_data["subject"],
                grade=quiz_data["grade"],
                description=quiz_data["description"]
            )

            for question_data in quiz_data["questions"]:
                question = quiz.questions.create(
                    text=question_data["question_text"]
                )
                for answer_data in question_data["answers"]:
                    question.answers.create(
                        text=answer_data["answer_text"],
                        is_correct=answer_data["is_correct"]
                    )


# class QuizDetailView(View):
#     def get(self, request, quiz_id, *args, **kwargs):
#         quiz = Quiz.objects.get(id=quiz_id)
#         questions = quiz.questions.all()
#
#         context = {
#             'quiz': quiz,
#             'questions': questions,
#         }
#         return render(request, 'quiz_structure/quiz_detail.html', context)


# views.py


class CreateQuizView(LoginRequiredMixin, View):
    template_name = 'quiz_structure/create_quiz.html'

    def get(self, request):
        form = QuizForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = QuizForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            print("POST data:", request.POST)
            quiz = form.save(commit=False)
            quiz.creator = request.user
            quiz.save()

            question_formset = QuestionFormSet(request.POST)
            answer_formset = AnswerFormSet(request.POST)

            if question_formset.is_valid() and answer_formset.is_valid():

                for question_form in question_formset:
                    question = question_form.save(commit=False)
                    question.quiz = quiz
                    question.save()

                    for answer_form in answer_formset:
                        answer = answer_form.save(commit=False)
                        answer.question = question
                        answer.save()

                return redirect('quiz_detail', pk=quiz.id)
            else:
                messages.error(request, 'There was an issue with the form.')
        return render(request, self.template_name, {'form': form})




@login_required
def add_questions(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    if request.method == "POST":
        question_form = QuestionForm(request.POST)
        if question_form.is_valid():
            question = question_form.save(commit=False)
            question.quiz = quiz
            question.save()
            return redirect('add_answers', question_id=question.id)
    else:
        question_form = QuestionForm()
    return render(request, 'quiz_structure/add_questions.html', {'quiz': quiz, 'question_form': question_form})


@login_required
def add_answers(request, question_id):
    question = Question.objects.get(id=question_id)
    if request.method == "POST":
        answer_form = AnswerForm(request.POST)
        if answer_form.is_valid():
            answer = answer_form.save(commit=False)
            answer.question = question
            answer.save()
            return redirect('add_answers', question_id=question.id)  # Reload for another answer
    else:
        answer_form = AnswerForm()
    return render(request, 'quiz_structure/add_answers.html', {'question': question, 'answer_form': answer_form})


class QuizSearchAPIView(APIView):
    def get(self, request, *args, **kwargs):
        subject = request.GET.get("subject", "").strip()
        grade = request.GET.get("grade", "").strip()

        quizzes = Quiz.objects.all()

        if subject:
            quizzes = quizzes.filter(subject__icontains=subject)
        if grade:
            quizzes = quizzes.filter(grade__icontains=grade)


        quiz_data = [
            {
                "id": quiz.id,
                "title": quiz.title,
                "description": quiz.description,
                "subject": quiz.subject,
                "grade": quiz.grade,
                "created_at": quiz.created_at,
                "updated_at": quiz.updated_at,
                "creator": quiz.creator.username
            }
            for quiz in quizzes
        ]

        return Response(quiz_data, status=status.HTTP_200_OK)


class QuizAPIView(APIView):

    def get(self, request, quiz_id, *args, **kwargs):
        quiz = get_object_or_404(Quiz, id=quiz_id)
        questions = quiz.questions.all()

        quiz_data = {
            "id": quiz.id,
            "title": quiz.title,
            "description": quiz.description,
            "questions": [
                {
                    "id": question.id,
                    "text": question.text,
                    "answers": [
                        {"id": answer.id, "text": answer.text}
                        for answer in question.answers.all()
                    ],
                }
                for question in questions
            ],
        }

        return Response(quiz_data, status=status.HTTP_200_OK)

    def post(self, request, quiz_id, *args, **kwargs):
        quiz = get_object_or_404(Quiz, id=quiz_id)
        user_answers = request.data.get("answers", {})
        questions = quiz.questions.all()

        total_questions = questions.count()
        correct_count = 0

        for question in questions:
            correct_answer = question.answers.filter(is_correct=True).first()
            user_answer_id = user_answers.get(str(question.id))

            if correct_answer and str(correct_answer.id) == user_answer_id:
                correct_count += 1

        grade = round((correct_count / total_questions) * 4 + 2, 2) if total_questions > 0 else 2

        return Response(
            {
                "correct_count": correct_count,
                "total_questions": total_questions,
                "grade": grade,
                "percentage": (correct_count / total_questions) * 100 if total_questions > 0 else 0,
            },
            status=status.HTTP_200_OK,
        )


class QuizDetailView(View):

    def get(self, request, pk, *args, **kwargs):
        quiz = get_object_or_404(Quiz, pk=pk)
        return render(request, 'quiz_structure/quiz_detail.html', {'quiz': quiz})

# test