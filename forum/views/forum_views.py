from django.views import generic
from forum.models import Topic


class TopicListView(generic.ListView):
    model = Topic
    paginate_by = 25
    template_name = 'forum/topics/list.html'


class TopicDetailView(generic.DetailView):
    model = Topic
    template_name = 'forum/topics/detail.html'
