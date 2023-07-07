from rest_framework import generics
from posts.models import Posts
from posts.serializers import PostsDetailSerializer, PostsListCreateSerializer


class PostsListCreateView(generics.ListCreateAPIView):
    queryset = Posts.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return PostsListCreateSerializer
        return PostsListCreateSerializer


class PostsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Posts.objects.all()

    def get_serializer_class(self):
        if self.request.method == ['POST', 'PATCH']:
            return PostsDetailSerializer
        return PostsDetailSerializer
