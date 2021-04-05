from . import views
from django.urls import path,include
from rest_framework import routers
from django.contrib.auth.decorators import login_required

router = routers.DefaultRouter()
router.register(r'posts', views.PostViewSet)

urlpatterns = [
 path('', views.start, name='piazza'),
 path('posts/', login_required(views.PostView.as_view(template_name='posts.html'))),
 path('createpost/', views.createPost, name='createPost'),
 path('comment/', views.comment, name='comment'),
]

