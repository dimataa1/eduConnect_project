from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.views import View

from .forms import CustomUserForm, CustomLoginForm
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib import messages


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


def base_view(request):
    return render(request, 'common/base.html')


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
