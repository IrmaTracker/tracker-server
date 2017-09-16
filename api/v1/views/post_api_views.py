from rest_framework import viewsets
from tracker.models import Post
from api.v1.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
