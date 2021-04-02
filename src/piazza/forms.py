from django import forms
from .models import Post,Topic

OPTIONS = (
        ("Sports", "Sports"),
        ("Politics", "Politics"),
        ("Tech", "Tech"),
        (4, "Health"),
        )

""" class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['name']
         """



genre_choices = Topic.objects.all().values_list('id', 'name').distinct()

genre_choices_list = []

for item in genre_choices:
    genre_choices_list.append(item)
 




class TopicForm(forms.Form):
    #name = forms.ModelMultipleChoiceField(queryset=Topic.objects.all())

    class Meta:
        model = Topic
#choices=OPTIONS, widget=forms.CheckboxSelectMultiple

class CreatePost(forms.ModelForm):
    topics = forms.MultipleChoiceField(choices=genre_choices)
   # topics = forms.MultipleChoiceField(choices=OPTIONS, widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Post
        #exclude = ('user','timestamp','status','likes','dislikes','extimestamp','poster')
        fields = ('title', 'body','topics')
    
"""     def __init__(self, *args, **kwargs):
        super(CreatePost, self).__init__(*args, **kwargs)
        self.fields['topics'].initial = [c.pk for c in Post.object.all()]     """

   # def __init__(self, *args, **kwargs):
    #  super(CreatePost, self).__init__(*args, **kwargs)
       # self.fields['topics'].widgets = forms.widgets.CheckboxSelectMultiple()
     #  self.fields['topics'].queryset = Topic.objects.all()
    
   
