from rest_framework import serializers
from posts.models import Posts


class PostsListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        # queryset = Posts.objects.order_by('-id')
        fields = ('id', 'owner', 'title', 'image', 'posted_at', 'like_dislikes')


class PostsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        # queryset = Posts.objects.order_by('-id',)
        fields = ('id', 'owner', 'title', 'image', 'posted_at', 'like_dislikes')
        read_only_fields = ('id',)
