from rest_framework import serializers
from callapp.models import Post


class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ('name', 'link', 'place', 'time', 'status')