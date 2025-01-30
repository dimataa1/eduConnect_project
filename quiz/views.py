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


import json
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from .forms import QuizForm
from .models import Quiz, Question, Answer


class CreateQuizView(View):
    template_name = 'quiz_structure/create_quiz.html'

    def get(self, request):
        quiz_form = QuizForm()
        return render(request, self.template_name, {'quiz_form': quiz_form})

    def post(self, request):
        quiz_form = QuizForm(request.POST)

        if quiz_form.is_valid():
            # Save quiz object
            quiz = quiz_form.save(commit=False)
            quiz.creator = request.user
            quiz.save()

            # Debugging: Check if data is coming as expected
            print(f"Quiz created: {quiz.id} - {quiz.title}")

            # Get question and answer data from the request
            data = request.POST
            questions_data = []

            # Collecting all questions and answers
            for key in data:
                if key.startswith("questions["):
                    question_id = key.split('[')[1].split(']')[0]
                    question_text = data[key]

                    # Collect answers for the current question
                    answers = []
                    for i in range(1, 5):  # assuming max 4 answers
                        answer_key = f"answers_{question_id}_{i}"
                        if answer_key in data:
                            answers.append(data[answer_key])

                    questions_data.append({
                        'question_text': question_text,
                        'answers': answers,
                        'correct_answer': data.get(f'correct_answer_{question_id}')
                    })

            # Now save the questions and answers
            for question_data in questions_data:
                question = Question.objects.create(
                    quiz=quiz,
                    text=question_data['question_text'],
                    question_type='MCQ'  # Assuming 'MCQ' type
                )

                # Save answers
                correct_answer_index = int(question_data['correct_answer'])
                for idx, answer_text in enumerate(question_data['answers']):
                    is_correct = (idx == correct_answer_index)
                    Answer.objects.create(
                        question=question,
                        text=answer_text,
                        is_correct=is_correct
                    )

            messages.success(request, "Quiz created successfully!")
            return redirect('quiz_detail', pk=quiz.id)

        else:
            messages.error(request, "Error creating quiz.")
            print(f"Quiz form errors: {quiz_form.errors}")

        return render(request, self.template_name, {'quiz_form': quiz_form})


@login_required
def add_questions(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    if request.method == "POST":
        question_form = QuestionForm(request.POST)
        if question_form.is_valid():
            question = question_form.save(commit=False)
            question.quiz = quiz
            question.save()
            print(f"Question added: {question.id} - {question.text}")
            return redirect('add_answers', question_id=question.id)
        else:
            print(f"Question form errors: {question_form.errors}")
    else:
        question_form = QuestionForm()
    return render(request, 'quiz_structure/add_questions.html', {'quiz': quiz, 'question_form': question_form})


@login_required
def add_answers(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    if request.method == "POST":
        answer_form = AnswerForm(request.POST)
        if answer_form.is_valid():
            answer = answer_form.save(commit=False)
            answer.question = question
            answer.save()
            print(f"Answer added: {answer.id} - {answer.text}")
            return redirect('add_answers', question_id=question.id)
        else:
            print(f"Answer form errors: {answer_form.errors}")
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
                        {"id": answer.id, "text": answer.text, "is_correct": answer.is_correct}
                        for answer in question.answers.all()
                    ],
                    "correct_answer_text": next(
                        (answer.text for answer in question.answers.all() if answer.is_correct),
                        None
                    )
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
        correct_answers = {}

        for question in questions:
            correct_answer = question.answers.filter(is_correct=True).first()
            user_answer_id = user_answers.get(str(question.id))

            if correct_answer:
                correct_answers[str(question.id)] = {
                    "id": correct_answer.id,
                    "text": correct_answer.text
                }

                if str(correct_answer.id) == user_answer_id:
                    correct_count += 1

        grade = round((correct_count / total_questions) * 4 + 2, 2) if total_questions > 0 else 2

        return Response(
            {
                "correct_count": correct_count,
                "total_questions": total_questions,
                "grade": grade,
                "percentage": (correct_count / total_questions) * 100 if total_questions > 0 else 0,
                "correct_answers": correct_answers,  # Sending correct answers to frontend
            },
            status=status.HTTP_200_OK,
        )


class QuizDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        quiz = get_object_or_404(Quiz, pk=pk)
        return render(request, 'quiz_structure/quiz_detail.html', {'quiz': quiz})
