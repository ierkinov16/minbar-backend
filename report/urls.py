from django.urls import path
from report.views import ReportDetailView, ReportListCreateView

urlpatterns = [
    path('', ReportListCreateView.as_view(), name='report_list_create'),
    path('<int:pk>', ReportDetailView.as_view(), name='report_detail')
]
