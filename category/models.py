from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    profile_image = models.ImageField
    image_banner = models.ImageField

    def __str__(self):
        return f"{self.name} ({self.created_date})"
