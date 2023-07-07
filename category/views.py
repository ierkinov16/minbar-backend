from rest_framework import generics
from category.serializers import CategorySerializer, CategoryDetailSerializer
from category.models import Category


class CategoryListCreateView(generics.ListAPIView):
    queryset = Category.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CategorySerializer
        return CategorySerializer


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    lookup_field = 'id'

    def get_serializer_class(self):
        if self.request.method in ['POST', 'PATCH']:
            return CategoryDetailSerializer
        return CategoryDetailSerializer
