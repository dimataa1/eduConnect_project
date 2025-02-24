from django import forms
from django.forms import modelformset_factory

from quiz.models import Quiz, Question, Answer


class QuizSearchForm(forms.Form):
    subject = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Търси по предмет'
        })
    )
    grade = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Търси по клас'
        })
    )


class FileUploadForm(forms.Form):
    file = forms.FileField(
        required=True,
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control',
            'accept': '.pdf,.doc,.docx,.txt'
        })
    )


class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['title', 'description', 'subject', 'grade']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Заглавие'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Описание'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Предмет'}),
            'grade': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Клас'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if field.initial is None:
                field.initial = ''
            if isinstance(field.widget, forms.TextInput) or isinstance(field.widget, forms.Textarea):
                if not field.initial:
                    field.initial = ''


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text']


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['text', 'is_correct']


# Formsets
QuestionFormSet = modelformset_factory(Question, form=QuestionForm, extra=1)
AnswerFormSet = modelformset_factory(Answer, form=AnswerForm, extra=4)
