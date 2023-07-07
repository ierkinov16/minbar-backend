from django.db import models


# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=100, blank=True)
    owner = models.ForeignKey('clerics.Clerics', on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField
    description = models.TextField
    posted_at = models.DateTimeField

    def __str__(self):
        f"{self.title} : {self.posted_at}"
