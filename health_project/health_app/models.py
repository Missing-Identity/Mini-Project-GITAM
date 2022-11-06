from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    post_pic = models.ImageField(upload_to='post_pics/')
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=200)
    author = models.CharField(max_length=200, null=True)
    created_date = models.DateTimeField(default=timezone.now())
    food_name = models.CharField(max_length=200, null=True, blank=True)
    calorie_count = models.CharField(max_length=200, null=True)