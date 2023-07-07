from rest_framework import generics
from category.models import Category
from serializers import CategorySerializer, CategoryDetailSerializer


class CategoryListCreateView(generics.ListAPIView):
    queryset = Category.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CategorySerializer
        return CategorySerializer


class CategoryDetailVie(generics.RetrieveUpdateDestroyAPIView):
