from django.db import models


# Create your models here.
class Report(models.Model):
    class ReportTypes(models.TextChoices):
        REPORT1 = 'CONTENT CATEGORY REPORT'
        REPORT2 = 'CONTENT QUALITY REPORT'
        REPORT3 = 'USER GENERATED REPORT'
        REPORT4 = 'CONTENT FEEDBACK REPORT'

    reporter_author = models.CharField(max_length=100, blank=True)
    report_time = models.DateTimeField(auto_now_add=True)
    report_to = models.ForeignKey('clerics.Clerics', on_delete=models.CASCADE, related_name='report_to')
    report_type = models.CharField(max_length=255, choices=ReportTypes.choices)
    why_report = models.TextField(max_length=255, blank=True)


