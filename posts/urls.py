from django.urls import path
from posts.views import PostsDetailView, PostsListCreateView

urlpatterns = [
    path('', PostsListCreateView.as_view(), name='posts_list_create'),
    path('<int:pk>', PostsDetailView.as_view(), name='posts_detail'),


]
