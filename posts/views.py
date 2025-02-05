from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import F, Value, DateTimeField
from django.db.models.functions import Cast
from django.http import HttpResponseBadRequest, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from common.serializers import PostSerializer
from quiz.models import Quiz
from .forms import PostForm, CommentForm, SchoolForm, ScheduleTourForm
from django.contrib import messages

from .models import Post, School, Comment, Vote, Tour
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
            return HttpResponseRedirect(reverse('dashboard'))

        return render(request, self.template_name, {'form': form})


class CreateTourView(LoginRequiredMixin, View):
    template_name = 'tour_structure/create_tour.html'

    def get(self, request):
        form = ScheduleTourForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ScheduleTourForm(request.POST, request.FILES)
        if form.is_valid():
            tour = form.save(commit=False)
            tour.teacher = request.user
            tour.save()
            messages.success(request, "Tour scheduled successfully!")
            return redirect('home')
        else:
            messages.error(request, "There was an error scheduling the tour.")
        return render(request, self.template_name, {'form': form})


class DashBoardListView(ListView):
    template_name = 'common/dashboard.html'
    context_object_name = 'items_with_type'

    def get_queryset(self):
        user = self.request.user
        posts = Post.objects.filter(author=user)
        tours = Tour.objects.filter(teacher=user)
        quizzes = Quiz.objects.filter(creator=user)

        combined = list(posts) + list(tours) + list(quizzes)
        return combined

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        items_list = context['items_with_type']
        paginator = Paginator(items_list, 3)

        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context['page_obj'] = page_obj

        context['items_with_type'] = [
            {'item': item, 'type': 'Post' if isinstance(item, Post) else 'Tour' if isinstance(item, Tour) else 'Quiz'}
            for item in page_obj.object_list
        ]
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_structure/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = context['post']

        comments = post.comments.annotate(
            rating=F('up_votes') - F('down_votes')
        ).order_by('-rating')

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
            comments = post.comments.annotate(
                rating=F('up_votes') - F('down_votes')
            ).order_by('-rating')
            context = {
                'post': post,
                'comments': comments,
                'form': form
            }
            return self.render_to_response(context)


class TourDetailView(DetailView):
    model = Tour
    template_name = 'tour_structure/tour_detail.html'
    context_object_name = 'tour'


class PostEditView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post_structure/post_edit.html'
    context_object_name = 'post'

    def get_success_url(self):
        return reverse_lazy('dashboard')


class TourEditView(LoginRequiredMixin, UpdateView):
    model = Tour
    form_class = ScheduleTourForm
    template_name = 'tour_structure/tour_edit.html'
    context_object_name = 'tour'

    def get_queryset(self):
        return Tour.objects.filter(teacher=self.request.user)

    def form_valid(self, form):
        messages.success(self.request, "Tour updated successfully!")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('dashboard')


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_structure/post_confirm_delete.html'
    context_object_name = 'post'

    def get_success_url(self):
        return reverse_lazy('dashboard')


class TourDeleteView(LoginRequiredMixin, DeleteView):
    model = Tour
    template_name = 'tour_structure/tour_confirm_delete.html'
    context_object_name = 'tour'

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


class TourListView(ListView):
    model = Tour
    template_name = 'tour_structure/tour_list.html'
    context_object_name = 'tours'

    def get_queryset(self):
        query = self.request.GET.get('search', '')
        queryset = Tour.objects.all().order_by('date')
        if query:
            queryset = queryset.filter(name__icontains=query)
        if self.request.GET.get('location'):
            queryset = queryset.filter(location__icontains=self.request.GET.get('location'))
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = Paginator(self.get_queryset(), 5)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context['page_obj'] = page_obj
        return context


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


@login_required
def vote_comment(request, post_id, comment_id, vote_action):
    comment = get_object_or_404(Comment, id=comment_id)

    existing_vote = Vote.objects.filter(user=request.user, comment=comment).first()

    if existing_vote:

        if existing_vote.vote_type == vote_action:
            return JsonResponse({'error': 'You have already voted this way on this comment'}, status=400)
        else:
            # Update the vote if the action is different
            if existing_vote.vote_type == 'upvote':
                comment.up_votes -= 1
            elif existing_vote.vote_type == 'downvote':
                comment.down_votes -= 1
            existing_vote.vote_type = vote_action
    else:

        existing_vote = Vote(user=request.user, comment=comment, vote_type=vote_action)
        if vote_action == 'upvote':
            comment.up_votes += 1
        elif vote_action == 'downvote':
            comment.down_votes += 1

    comment.save()
    existing_vote.save()

    return JsonResponse({'new_rating': comment.rating})
