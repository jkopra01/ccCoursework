from django import forms
from .models import Post,Topic

""" class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['name']
         """

class CreatePost(forms.ModelForm):
    topics = forms.MultipleChoiceField(label="Topic", widget=forms.CheckboxSelectMultiple, choices=Topic.OPTIONS)
    class Meta:
        model = Post
        #exclude = ('user','timestamp','status','likes','dislikes','extimestamp','poster')
        fields = ('title', 'body','topics',)
    
        
"""     def __init__(self, *args, **kwargs):
        super(CreatePost, self).__init__(*args, **kwargs)
        self.fields['topics'].widgets = forms.widgets.CheckboxSelectMultiple()
        self.fields['topics'].queryset = Topic.objects.all() """

