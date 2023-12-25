from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserAccount(models.Model):

    user = models.OneToOneField(User,on_delete = models.CASCADE)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique = True)
    department = models.CharField(blank=True, default=None, max_length=255)
    profile_pic = models.ImageField(blank=True, upload_to = "profile_pics",default=None)
    def save(self,*args,**kwargs):
        self.username = self.user.username
        self.email = self.user.email
        super().save(*args,**kwargs)

    def __str__(self):
        return self.username
