
from django import forms
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
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
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Въведи своя имейл'}),
        label="Email"
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Въведи паролата си'}),
        label="Password",
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            user = authenticate(email=email, password=password)
            if not user:
                raise forms.ValidationError("Невалиден имейл или парола")
        return cleaned_data


class LogoutForm(forms.Form):
    confirm = forms.BooleanField(required=True, label="Confirm Logout")


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'description', 'age', 'grade', 'subject', 'profile_picture']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': "Напиши кратко описание за себе си"}),
            'grade': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "пример: 10"}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "пример: Математика"}),
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


class CustomPasswordChangeForm(forms.Form):
    current_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Въведете текущата си парола'}),
        label="Текуща парола"
    )
    new_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Въведете новата си парола'}),
        label="Нова парола"
    )
    confirm_new_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Потвърдете новата си парола'}),
        label="Потвърдете новата парола"
    )

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get("new_password")
        confirm_new_password = cleaned_data.get("confirm_new_password")

        if new_password != confirm_new_password:
            raise forms.ValidationError("Двете нови пароли не съвпадат!")

        return cleaned_data

    def save(self, user, commit=True):
        user.set_password(self.cleaned_data["new_password"])
        if commit:
            user.save()
        return user

@login_required
def profile_details_view(request, username):
    User = get_user_model()
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=user)

    return render(request, 'accounts_structure/profile_details.html', {'profile': profile})


@login_required
def profile_update_view(request, username):
    User = get_user_model()
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=user)

    if request.user != user:
        messages.error(request, "You cannot update another user's profile.")
        return redirect('profile_details', username=request.user.username)

    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated successfully!")
            return redirect('profile_details', username=username)
        else:
            print(form.errors)
            messages.error(request, "There were some errors in your form. Please fix them below.")
    else:
        form = ProfileUpdateForm(instance=profile)

    return render(request, 'accounts_structure/profile_update.html', {'form': form})


@login_required
def change_password_view(request, username):
    User = get_user_model()
    user = get_object_or_404(User, username=username)

    if request.user != user:
        messages.error(request, "Не можете да променяте паролата на друг потребител.")
        return redirect('profile_details', username=request.user.username)

    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.POST)
        if form.is_valid():
            form.save(user)
            messages.success(request, "Паролата ви беше успешно променена!")
            return redirect('profile_details', username=username)
        else:
            messages.error(request, "Имаше грешки в формата. Моля, коригирайте ги.")
    else:
        form = CustomPasswordChangeForm()

    return render(request, 'accounts_structure/change_password.html', {'form': form, 'user': user})