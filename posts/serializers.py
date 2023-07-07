from rest_framework import serializers
from posts.models import Posts


class PostsListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        queryset = Posts.objects.all()
        fields = ('id', 'owner', 'title', 'image', 'posted_at')


class PostsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        queryset = Posts.objects.all()
        fields = ('id', 'owner', 'title', 'image', 'posted_at')
        read_only_fields = ('id',)
