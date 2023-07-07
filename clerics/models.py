from django.db import models


# Create your models here.

class Clerics(models.Model):
    name = models.CharField(max_length=50, blank=True)
    age = models.IntegerField
    description = models.CharField(max_length=400, blank=True)
    profile_image = models.ImageField()
    banner_image = models.ImageField
