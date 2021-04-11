from django import forms
from .models import Post,Topic,Comment
from datetime import datetime, timedelta
from django.utils import timezone
#from django.forms.widgets import SelectTimeWidget

def getDefaultExDate():
  return timezone.now() + timedelta(days=1)

topics = Topic.objects.all().values_list('id', 'name').distinct()
topics_list = []
for topic in topics:
    topics_list.append(topic)


class DateInput(forms.DateInput):
    input_type = 'date'

 

class CreatePost(forms.ModelForm):
    topics = forms.MultipleChoiceField(choices=topics_list,widget=forms.CheckboxSelectMultiple)
    extimestamp = forms.DateTimeField(initial=getDefaultExDate(), label='Expiry time:')
  
    class Meta:
        model = Post
        fields = ('title', 'body','topics','extimestamp')


class CreateComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)