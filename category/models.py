from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.ForeignKey('category.Category', on_delete=models.CASCADE, related_name='category')
    description = models.TextField
    created_date = models.DateTimeField(auto_now_add=True)
    profile_image = models.ImageField(null=True, blank=True)
    image_banner = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.created_date})"
