from django import forms
from forum.models import Topic


class TopicForm(forms.ModelForm):

    class Meta:
        model = Topic
        fields = ('name', 'content')