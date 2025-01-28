from django import forms
from .models import Post, Comment, School, Tour


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'image', 'subject', 'grade']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
            'grade': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Grade'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


class PostSearchForm(forms.Form):
    subject = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search by Subject'})
    )
    grade = forms.CharField(
        max_length=50,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search by Grade'})
    )


class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ['name', 'town', 'description', 'image']


class TourForm(forms.ModelForm):
    class Meta:
        model = Tour
        fields = ['school', 'description', 'date']
        widgets = {
            'school': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Provide a short description for the tour'
            }),
            'date': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local',
                'placeholder': 'Select date and time'
            }),
        }


class ScheduleTourForm(forms.ModelForm):
    class Meta:
        model = Tour
        fields = ['name', 'description', 'date', 'location', 'image', 'school']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tour Name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'school': forms.Select(attrs={'class': 'form-control'}),
        }


class TourSearchForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search by Name'})
    )
    location = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search by Location'})
    )
    date_from = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'From Date'})
    )
    date_to = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'To Date'})
    )


class TourDeleteConfirmationForm(forms.Form):
    confirm = forms.BooleanField(
        label="Are you sure you want to delete this tour?",
        required=True,
    )

class TourUpdateForm(forms.ModelForm):
    class Meta:
        model = Tour
        fields = ['name', 'description', 'date', 'location', 'image', 'school']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tour Name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Update Description'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Update Location'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'school': forms.Select(attrs={'class': 'form-control'}),
        }
