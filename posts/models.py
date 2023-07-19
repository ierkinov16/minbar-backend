from django.db import models


# Create your models here.
class Posts(models.Model):
    class PostsLikeDislikes(models.TextChoices):
        LIKE = '1'
        DISLIKE = '0'

    title = models.CharField(max_length=100, blank=True)
    owner = models.ForeignKey('clerics.Clerics', on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(null=True, blank=True)
    description = models.TextField()
    posted_at = models.DateTimeField()
    like_dislikes = models.CharField(max_length=10, choices=PostsLikeDislikes.choices, null=True)

    def __str__(self):
        f"{self.title} : {self.posted_at}"
