from rest_framework import serializers
from category.models import Category


class CategorySerializer(serializers.Serializer):
    class Meta:
        model = Category
        fields = ('name', 'created_at', 'profile_image', 'banner_image')


class CategoryDetailSerializer(serializers.Serializer):
    model = Category
    fields = ('name', 'created_at', 'profile_image', 'banner_image')
    read_only_fields = ('id',)
