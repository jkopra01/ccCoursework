from django.db import models
from django.conf import settings
from datetime import datetime, timedelta
from django.utils import timezone

# Gets the default expiry date of one day
def getDefaultExDate():
    return timezone.now() + timedelta(days=1)


class Topic(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


# Creates topics if the they dont exist yet
check_empty_obj = Topic.objects.all()
if not check_empty_obj:
    Topic.objects.bulk_create(
        [Topic(name="Sports"),
         Topic(name="Politics"),
         Topic(name="Tech"),
         Topic(name="Health")]
    )


class Comment(models.Model):
    commenter = models.CharField(max_length=60)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body


class PostAction(models.Model):
    user = models.CharField(max_length=60)
    action = models.CharField(max_length=60)
    timestamp = models.DateTimeField(auto_now_add=True)
    timeLeft = models.IntegerField()
    timeLeftMinutes = models.IntegerField()

    def __str__(self):
        return self.action


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    poster = models.CharField(max_length=60)
    title = models.CharField(max_length=60)
    topics = models.ManyToManyField(Topic)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    extimestamp = models.DateTimeField(default=getDefaultExDate())
    status = models.BooleanField(default=True)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    comments = models.ManyToManyField(Comment)
    postActions = models.ManyToManyField(PostAction)

    @property
    def is_live(self):
        return self.extimestamp > timezone.now()

    def __str__(self):
        return self.title