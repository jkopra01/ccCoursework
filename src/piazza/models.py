from django.db import models 
from django.conf import settings

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    poster = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=60)
    body = models.TextField()
    timestamp = models.DateTimeField(null=True, blank=True)
    extimestamp = models.DateTimeField(null=True, blank=True)
    status = models.BooleanField()
    likes = models.PositiveIntegerField()
    dislikes = models.PositiveIntegerField()
    def __str__(self):
        return self.title

