from rest_framework import generics
from clerics.models import Clerics
from clerics.serializers import ClericsListSerializer, ClericsDetailSerializer


# Create your views here.


class ClericsListCreateView(generics.ListCreateAPIView):
    queryset = Clerics.objects.order_by('-id')

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ClericsListSerializer
        return ClericsListSerializer


class ClericsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Clerics.objects.order_by('-id')
    lookup_field = 'id'

    def get_serializer_class(self):
        if self.request.method in ['POST', 'PATCH']:
            return ClericsDetailSerializer
        return ClericsDetailSerializer
