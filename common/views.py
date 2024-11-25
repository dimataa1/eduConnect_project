from django.shortcuts import render
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from posts.models import Post
from .forms import PostSearchForm
from .serializers import PostSerializer

class HomeView(View):
    def get(self, request, *args, **kwargs):
        # Handling when the user is authenticated
        if request.user.is_authenticated:
            context = {
                'username': request.user.username,
                'form': PostSearchForm(),
            }
            return render(request, 'common/landing_page_with_user.html', context)
        else:
            # If the user is not authenticated
            return render(request, 'common/landing_page_no_user.html')


class PostSearchAPIView(APIView):
    def get(self, request, *args, **kwargs):
        subject = request.GET.get('subject', '').strip()
        grade = request.GET.get('grade', '').strip()

        posts = Post.objects.all()

        if subject:
            posts = posts.filter(subject__icontains=subject)
        if grade:
            posts = posts.filter(grade__icontains=grade)

        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
