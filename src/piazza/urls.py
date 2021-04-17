from . import views
from django.urls import path, include
from rest_framework import routers
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(views.PostView.as_view(template_name='posts.html'))),
    path('posts/', login_required(views.PostView.as_view(template_name='posts.html'))),
    path('createpost/', views.createPost, name='createPost'),
    path('comment/', views.comment, name='comment'),
]
