from django.urls import path
from clerics.views import ClericsListCreateView, ClericsDetailView

urlpatterns = [
    path('', ClericsListCreateView.as_view(), name='clerics_list_create'),
    path('<int:pk>', ClericsDetailView.as_view(), name='clerics_detail'),
]
