
import django_filters
from .models import Topic,Post
class BookFilter(django_filters.FilterSet):
    topics = django_filters.ModelMultipleChoiceFilter(queryset=Topic.objects.all())
    class Meta:
        model = Post
        fields = ['topics']