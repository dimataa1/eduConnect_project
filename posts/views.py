from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView, DeleteView

from .forms import PostForm, CommentForm
from django.contrib import messages

from .models import Post


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
        return Post.objects.filter(author=self.request.user).order_by('-created_at')

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_structure/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['comment_form'] = CommentForm()
        context['comments'] = self.object.comments.all()
        return context


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