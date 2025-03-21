
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, update_session_auth_hash, get_user_model
from django.views import View
from django.views.generic import DetailView, DeleteView

from .forms import CustomUserForm, CustomLoginForm, ProfileUpdateForm, CustomPasswordChangeForm
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Profile, AppUser



def register(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            if user.role == 'teacher':
                user.is_approved = False
            user.save()

            Profile.objects.get_or_create(user=user)

            if user.role == 'teacher':
                return redirect('pending-approval')
            return redirect('home')
    else:
        form = CustomUserForm()
    return render(request, 'accounts_structure/register.html', {'form': form})


class LoginView(FormView):
    template_name = "accounts_structure/login.html"
    form_class = CustomLoginForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = authenticate(self.request, email=email, password=password)

        if user is not None:
            login(self.request, user)

            # Check if the user has a profile, if not, create one
            Profile.objects.get_or_create(user=user)

            return super().form_valid(form)
        else:
            messages.error(self.request, "Невалиден имейл или парола!")
            return self.form_invalid(form)


class LogoutView(View):

    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect('home')

    def get(self, request, *args, **kwargs):
        return render(request, 'accounts_structure/logout.html')


@login_required
def delete_profile_picture(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    profile = get_object_or_404(Profile, user=user)

    if request.user != user:
        messages.error(request, "You cannot delete another user's profile picture.")
        return redirect('profile_details', username=request.user.username)

    if profile.profile_picture:
        profile.delete_profile_picture()
        messages.success(request, "Successfully deleted your profile picture!")
    else:
        messages.warning(request, "No profile picture to delete.")

    return redirect('profile_details', username=username)


@login_required
def delete_profile(request, username):
    user = get_object_or_404(get_user_model(), username=username)

    if request.user != user:
        messages.error(request, "You cannot delete another user's profile.")
        return redirect('profile_details', username=request.user.username)

    profile = get_object_or_404(Profile, user=user)
    profile.delete_profile_picture()  #

    user.delete()

    messages.success(request, "Your profile has been successfully deleted!")

    return redirect('logout')

