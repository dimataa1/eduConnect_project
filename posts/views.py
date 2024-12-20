from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from common.serializers import PostSerializer
from .forms import PostForm, CommentForm, SchoolForm
from django.contrib import messages

from .models import Post, School
from .serializers import SchoolSerializer


class CreatePostView(LoginRequiredMixin, View):
    template_name = 'post_structure/main_post.html'

    def get(self, request):
        form = PostForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "Post created successfully!")
            return redirect('home')
        messages.error(request, "There was an error creating the post.")
        return render(request, self.template_name, {'form': form})


class DashBoardListView(ListView):
    model = Post
    template_name = 'common/dashboard.html'
    context_object_name = 'posts'

    def get_queryset(self):
        # Fetch posts specific to the logged-in user, ordered by creation date
        return Post.objects.filter(author=self.request.user).order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts_list = context['posts']

        # Paginate the posts
        paginator = Paginator(posts_list, 3)  # 5 posts per page
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context['page_obj'] = page_obj
        return context

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_structure/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = context['post']
        comments = post.comments.all()

        form = CommentForm()

        context['comments'] = comments
        context['form'] = form

        return context

    def post(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()

            return redirect('post_detail', pk=post.pk)
        else:
            comments = post.comments.all()
            context = {
                'post': post,
                'comments': comments,
                'form': form
            }
            return self.render_to_response(context)


class PostEditView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post_structure/post_edit.html'
    context_object_name = 'post'

    def get_success_url(self):
        return reverse_lazy('dashboard')


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_structure/post_confirm_delete.html'
    context_object_name = 'post'

    def get_success_url(self):
        return reverse_lazy('dashboard')


def school_list(request):
    query = request.GET.get('search', '')
    if query:
        schools = School.objects.filter(town__icontains=query)
    else:
        schools = School.objects.all()

    paginator = Paginator(schools, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'schools': schools,
        'search_query': query
    }
    return render(request, 'school_structure/school_list.html', context)


def school_detail(request, school_id):
    school = School.objects.get(id=school_id)
    return render(request, 'school_structure/school_detail.html', {'school': school})


def add_school(request):
    if request.method == 'POST':
        form = SchoolForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('school_list')
    else:
        form = SchoolForm()
    return render(request, 'school_structure/add_school.html', {'form': form})


def post_list(request):
    query = request.GET.get('search', '')
    if query:
        posts = Post.objects.filter(title__icontains=query).order_by('-created_at')
    else:
        posts = Post.objects.all().order_by('-created_at')

    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'search_query': query
    }
    return render(request, 'post_structure/post_list.html', context)