from django.shortcuts import redirect
from django.urls import resolve


class CheckTeacherApprovalMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            return self.get_response(request)
        current_url_name = resolve(request.path_info).url_name
        excluded_urls = ['register', 'login', 'pending-approval']
        if current_url_name in excluded_urls:
            return self.get_response(request)
        if request.user.role == 'teacher' and not request.user.is_approved:
            return redirect('pending-approval')
        return self.get_response(request)
