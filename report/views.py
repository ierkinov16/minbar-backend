from rest_framework import generics
from report.serializers import ReportDetailSerializer, ReportListCreateSerializer
from report.models import Report


class ReportListCreateView(generics.ListCreateAPIView):
    queryset = Report.objects.order_by('-id')

    def get_queryset(self):
        if self.request.method == 'POST':
            return ReportListCreateSerializer
        return ReportListCreateSerializer


class ReportDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Report.objects.order_by('-id')

    def get_serializer_class(self):
        if self.request.method in ['POST', 'PATCH']:
            return ReportDetailSerializer
        return ReportDetailSerializer
