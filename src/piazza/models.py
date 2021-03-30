from django.db import models 
from django.conf import settings

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    poster = models.CharField(max_length=60)
    title = models.CharField(max_length=60)
    body = models.TextField()
    timestamp = models.DateTimeField(null=True, blank=True)
    extimestamp = models.DateTimeField(null=True, blank=True)
    status = models.BooleanField(default=True)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.title

