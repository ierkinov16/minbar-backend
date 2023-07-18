from rest_framework import serializers
from clerics.models import Clerics


class ClericsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clerics
        fields = ('name', 'age', 'description', 'profile_image', 'banner_image')


class ClericsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clerics
        fields = ('name', 'description', 'profile_image', 'banner_image')
        read_only_fields = ('id',)
