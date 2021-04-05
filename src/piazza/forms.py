from django import forms
from .models import Post,Topic,Comment

topics = Topic.objects.all().values_list('id', 'name').distinct()
topics_list = []
for topic in topics:
    topics_list.append(topic)
 

class CreatePost(forms.ModelForm):
    topics = forms.MultipleChoiceField(choices=topics_list,widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Post
        fields = ('title', 'body','topics')


class CreateComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)