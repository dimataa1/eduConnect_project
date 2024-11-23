from django.shortcuts import render

from django.shortcuts import render
from django.views import View


class HomeView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(request, 'common/landing_page_with_user.html')
        else:
            return render(request, 'common/landing_page_no_user.html')
