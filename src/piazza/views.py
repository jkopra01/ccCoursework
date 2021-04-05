from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.utils import timezone
from django.template import RequestContext
from django.views.generic.base import TemplateView
from datetime import timedelta,datetime
from rest_framework import viewsets
from .serializers import PostSerializer
from .models import Post,Topic
from .forms import CreatePost,CreateComment
from django.db.models import F


class PostViewSet(viewsets.ModelViewSet):
 queryset = Post.objects.all().order_by('title')
 serializer_class = PostSerializer


class PostView(TemplateView):
    template_name = "posts.html"

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        liked = False
        disliked = False
        context['topics'] = Topic.objects.all()
        topic = self.request.GET.get('topic')
        likes = self.request.GET.get('like')
        dislikes = self.request.GET.get('dislike')
        dontLike = self.request.GET.get('dontLike')
        dontDislike = self.request.GET.get('dontDislike')
        if likes:
            Post.objects.filter(id=likes).update(likes=F('likes') + 1)
            liked = True
        if dontLike:
            Post.objects.filter(id=dontLike).update(likes=F('likes') - 1)
            liked = False
        if dislikes:
            Post.objects.filter(id=dislikes).update(dislikes=F('dislikes') + 1)
            disliked = True
        if dontDislike:
            Post.objects.filter(id=dontDislike).update(dislikes=F('dislikes') - 1)
            disliked = False

        context['liked'] = liked
        context['disliked'] = disliked
        context['filter'] = Post.objects.all()
        if topic:
            context['filter'] = Post.objects.filter(topics=topic)
        return context


@login_required
def start(request):
    latest_post_list = Post.objects.all().order_by('-timestamp')
   # topic = 
 #   posts = latest_post_list.objects.filter(topics=topic)
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
            return redirect('/posts/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


#creates post and saves many to many relationship
def createPost(request):
    if request.method == "POST":
        form = CreatePost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.poster = request.user
            post.save()
            form.save_m2m() 
            return redirect('/posts/')
    else:
        form = CreatePost()
    return render(request, 'createpost.html', {'form': form})


def comment(request):
    if request.method == "POST":
        postId = request.GET.get('comment')
        post = Post.objects.get(id=postId)
        form = CreateComment(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.commenter = request.user
            postId = request.GET.get('comment')
            
           # context['postToComment'] = Post.objects.get(id=postId)
            comment.save()
            form.save_m2m() 
            post.comments.add(comment)
            return redirect('/posts/')
    else:
        form = CreateComment()
        postId = request.GET.get('comment')
        post = Post.objects.get(id=postId)
    return render(request, 'comment.html', {'form': form, 'post':post})