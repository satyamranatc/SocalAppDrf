from django.db import models

# Create your models here.


# Custom User.
class User(models.Model):
    FullName = models.CharField(max_length=255)
    ProfilePic = models.CharField(max_length=555,default='', blank=True)
    UserName = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)
