from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect, get_object_or_404

from accounts.models import Profile


class CustomUserForm(UserCreationForm):
    role = forms.ChoiceField(
        choices=[('student', 'Student'), ('teacher', 'Teacher')],
        required=True,
        label="Register as",
    )

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'role', 'password1', 'password2')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = "__all__"


class CustomLoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
        label="Email"
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'}),
        label="Password"
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            user = authenticate(email=email, password=password)
            if not user:
                raise forms.ValidationError("Invalid email or password")
        return cleaned_data


class LogoutForm(forms.Form):
    confirm = forms.BooleanField(required=True, label="Confirm Logout")


@login_required
def profile_details_view(request):
    profile = request.user.profile
    return render(request, 'accounts_structure/profile_details.html', {'profile': profile})


@login_required
def profile_update_view(request):
    profile = get_object_or_404(Profile, user=request.user)

    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_details')
        else:
            print(form.errors)
    else:
        form = ProfileUpdateForm(instance=profile)

    return render(request, 'accounts_structure/profile_update.html', {'form': form})


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'age', 'grade', 'subject', 'profile_picture']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'grade': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "e.g., 10th Grade"}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "e.g., Mathematics"}),
            'profile_picture': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        user = self.instance.user

        if user.role == 'teacher' and cleaned_data.get('grade'):
            cleaned_data['grade'] = None

        if user.role == 'student' and cleaned_data.get('subject'):
            cleaned_data['subject'] = None

        return cleaned_data
