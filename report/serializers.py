from rest_framework import serializers
from report.models import Report


class ReportListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ('id', 'reporter_author', 'report_time', 'report_to', 'report_type', 'why_report')


class ReportDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ('id', 'reporter_author', 'report_time', 'report_to', 'report_type', 'why_report')
        read_only_fields = ('id',)
