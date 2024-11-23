from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.views import View
from django.views.generic import DetailView

from .forms import CustomUserForm, CustomLoginForm
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

            if user.role == 'teacher':
                return redirect('pending-approval')
            return redirect('home')
    else:
        form = CustomUserForm()
    return render(request, 'accounts_structure/register.html', {'form': form})


class LoginView(FormView):
    template_name = "accounts_structure/login.html"
    form_class = CustomLoginForm
    success_url = reverse_lazy('home')  # Replace 'home' with your target page after login

    def form_valid(self, form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = authenticate(self.request, email=email, password=password)

        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            messages.error(self.request, "Invalid email or password.")
            return self.form_invalid(form)


class LogoutView(View):

    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect('home')

    def get(self, request, *args, **kwargs):

        return render(request, 'accounts_structure/logout.html')


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'accounts_structure/profile_details.html'
    context_object_name = 'profile'

    def get_object(self):
        profile = Profile.objects.filter(user=self.request.user).first()
        if profile is None:
            raise Http404("Profile does not exist.")
        return profile
