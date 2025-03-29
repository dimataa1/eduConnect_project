from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from chat.models import Thread



@login_required
def messages_page(request):
    User = get_user_model()

    threads = Thread.objects.by_user(user=request.user).prefetch_related('chatmessage_thread').order_by('timestamp')
    context = {
        'Threads': threads,
        'users': User.objects.all()
    }
    return render(request, 'chat_structure/messages.html', context)


@login_required
def chat_room(request, thread_id):

    thread = get_object_or_404(Thread, id=thread_id)

    # Ensure the current user is part of this thread
    if request.user != thread.first_person and request.user != thread.second_person:
        return redirect('home')

        # Determine the other user in the chat
    other_user = thread.first_person if thread.second_person == request.user else thread.second_person
    messages = thread.chatmessage_thread.all().order_by('timestamp')
    User = get_user_model()
    context = {

        'thread': thread,
        'other_user': other_user,
        'messages': messages,
        'users': User.objects.all()
    }
    return render(request, 'chat_structure/messages.html', context)


@login_required
def start_chat(request, user_id):
    User = get_user_model()
    other_user = get_object_or_404(User, id=user_id)

    # Check if a thread already exists between the users
    thread = Thread.objects.filter(
        (Q(first_person=request.user) & Q(second_person=other_user)) |
        (Q(first_person=other_user) & Q(second_person=request.user))
    ).first()

    # If no thread exists, create a new one
    if not thread:
        thread = Thread.objects.create(first_person=request.user, second_person=other_user)

    # Redirect to the chat room for the thread
    return redirect('chat_room', thread_id=thread.id)