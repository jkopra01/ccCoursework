from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('poster', 'title', 'body', 'timestamp',
                  'extimestamp', 'status', 'likes', 'dislikes')
