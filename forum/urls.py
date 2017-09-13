from django.conf.urls import url
from forum import views


app_name = "news"
urlpatterns = [
    url(r'^$', views.TopicListView.as_view(), name='topics'),
    url(r'^(?P<slug>[\w-]+)/$', views.TopicDetailView.as_view(), name='topic_detail'),
]