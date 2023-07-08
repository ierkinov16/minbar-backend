from rest_framework import serializers

from report.models import Report


class ReportListCreateSerializer(serializers.Serializer):
    class Meta:
        model = Report
        fields = ('id', 'reporter_author', 'report_date', 'report_time', 'report_to', 'report_type', 'why_report')


class ReportDetailSerializer(serializers.Serializer):
    class Meta:
        model = Report
        fields = ('id', 'reporter_author', 'report_date', 'report_time', 'report_to', 'report_type', 'why_report')
        read_only_fields = ('id',)
