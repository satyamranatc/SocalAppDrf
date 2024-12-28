from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    poster = models.CharField(max_length=255,default='', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

