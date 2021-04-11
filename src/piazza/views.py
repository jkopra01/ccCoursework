from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.utils import timezone
from django.template import RequestContext
from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404
from datetime import timedelta,datetime
from rest_framework import viewsets
from .serializers import PostSerializer
from .models import Post,Topic,PostAction
from .forms import CreatePost,CreateComment
from django.db.models import F

class PostViewSet(viewsets.ModelViewSet):
 queryset = Post.objects.all().order_by('title')
 serializer_class = PostSerializer


class PostView(TemplateView):
    template_name = "posts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        #check post statuses
        allPosts = Post.objects.all()
        timeNow = timezone.now() 
        for post in allPosts:
            if not post.in_progress:
                Post.objects.filter(id=post.id).update(status=False)

        topic = self.request.GET.get('topic')
        expiredTopic = self.request.GET.get('expiredTopic')
        likes = self.request.GET.get('like')
        dislikes = self.request.GET.get('dislike')
        dontLike = self.request.GET.get('dontLike')
        dontDislike = self.request.GET.get('dontDislike')

        user = self.request.user

        #get posts liked and disliked by the user
        likedPosts = Post.objects.filter(postActions__action="Liked", postActions__user = user).values_list('id', flat=True)
        dislikedPosts = Post.objects.filter(postActions__action="Disliked", postActions__user = user).values_list('id', flat=True)
        

        if likes:
                Post.objects.filter(id=likes).update(likes=F('likes') + 1)
                timeLeft =  Post.objects.get(id=likes).extimestamp-timezone.now()
                postAction = PostAction.objects.create(action="Liked", user=user, timeLeft= timeLeft.seconds//3600, timeLeftMinutes=(timeLeft.seconds//60)%60)
                post.postActions.add(postAction)
        if dontLike:
                Post.objects.filter(id=dontLike).update(likes=F('likes') - 1)
                postAction = get_object_or_404(PostAction, post=dontLike, user=user, action="Liked")
                Post.objects.get(id=dontLike).postActions.remove(postAction)
        if dislikes:
                Post.objects.filter(id=dislikes).update(dislikes=F('dislikes') + 1)
                timeLeft =  Post.objects.get(id=dislikes).extimestamp-timezone.now()
                postAction = PostAction.objects.create(action="Disliked", user=user, timeLeft= timeLeft.seconds//3600, timeLeftMinutes=(timeLeft.seconds//60)%60)
                post.postActions.add(postAction)
        if dontDislike:
                Post.objects.filter(id=dontDislike).update(dislikes=F('dislikes') - 1)
                postAction =  get_object_or_404(PostAction, post=dontDislike, user=user, action="Disliked")
                Post.objects.get(id=dontDislike).postActions.remove(postAction)


        #save variables for html
        context['likedPosts'] = likedPosts
        context['dislikedPosts'] = dislikedPosts
        context['username'] = user.username
        context['filter'] = Post.objects.all().order_by('-timestamp')
        context['topics'] = Topic.objects.all()

        if topic:
            context['test'] = topic
            posts = Post.objects.filter(topics=topic)
            context['filter'] = posts.annotate(fieldsum=F('dislikes') + F('likes')).order_by('-fieldsum')
        elif expiredTopic:
            context['test'] = expiredTopic
            posts = Post.objects.filter(topics=expiredTopic, status=False)
            context['filter'] = posts.annotate(fieldsum=F('dislikes') + F('likes')).order_by('-fieldsum')
        
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
        timeLeft = post.extimestamp-timezone.now()
        postAction = PostAction.objects.create(action="Commented", user=request.user, timeLeft= timeLeft.seconds//3600, timeLeftMinutes=(timeLeft.seconds//60)%60)
        form = CreateComment(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.commenter = request.user
            postId = request.GET.get('comment')
            comment.save()
            form.save_m2m() 
            post.comments.add(comment)
            post.postActions.add(postAction)

            return redirect('/posts/')
    else:
        form = CreateComment()
        postId = request.GET.get('comment')
        post = Post.objects.get(id=postId)
    return render(request, 'comment.html', {'form': form, 'post':post})