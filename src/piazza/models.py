from django.db import models 
from django.conf import settings
from datetime import datetime, timedelta
from django.utils import timezone


OPTIONS = (
        ("Sports", "Sports"),
        ("Politics", "Politics"),
        ("Tech", "Tech"),
        ("Health", "Health"),
        )

#Gets the default expiry date of one day
def getDefaultExDate():
  return timezone.now() + timedelta(days=1)

class Topic(models.Model):
    OPTIONS = (
        ("Sports", "Sports"),
        ("Politics", "Politics"),
        ("Tech", "Tech"),
        ("Health", "Health"),
        )
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

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
    def __str__(self):
        return self.title

