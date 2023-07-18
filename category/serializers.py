from rest_framework import serializers
from category.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'created_date', 'description', 'profile_image', 'image_banner')


class CategoryDetailSerializer(serializers.ModelSerializer):
    model = Category
    fields = ('name', 'created_date', 'description', 'profile_image', 'image_banner')
    read_only_fields = ('id',)
