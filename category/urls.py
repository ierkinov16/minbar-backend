from django.urls import path
from category.views import CategoryListCreateView, CategoryDetailView

urlpatterns = [
    path('', CategoryListCreateView.as_view(), name='category_list_create'),
    path('<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),

]
