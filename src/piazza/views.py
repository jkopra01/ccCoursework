from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.utils import timezone
from datetime import timedelta
from rest_framework import viewsets
from .serializers import PostSerializer
from .models import Post
from .forms import CreatePost


class PostViewSet(viewsets.ModelViewSet):
 queryset = Post.objects.all().order_by('title')
 serializer_class = PostSerializer


@login_required
def start(request):
    latest_post_list = Post.objects.all().order_by('-timestamp')
    context = {'latest_post_list':latest_post_list}
    return render(request, 'index.html', context)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


@login_required()
def createPost(request):
    if request.method == "POST":
        form = CreatePost(request.POST, initial={'status': True})
        if form.is_valid():
            form.likes = 0
            form.dislikes = 0
            form.timestamp = timezone.now()
            form.extimestamp = timezone.now() + timedelta(1)
            form.poster = request.user
            form.status = True
            form.save()
            return redirect('/')
    else:
        form = CreatePost()
    return render(request, 'createpost.html', {'form': form})



""" @login_required()
def createPost(request):
    user = request.user
    form = CreatePost(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            sender = user
            title = form.cleaned_data.get("title")
            b = CreatePost.objects.create(title=title)
            b.save()
            return redirect('/')
    else:
        form = Post()
    return render(request, 'createpost.html', {'form': form}) """