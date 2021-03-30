from django import forms
from .models import Post

class CreatePost(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('user','timestamp','status','likes','dislikes','extimestamp')
        fields = ('title', 'body')