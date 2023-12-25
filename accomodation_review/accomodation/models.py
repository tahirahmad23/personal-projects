from django.db import models
from accounts.models import UserAccount
# Create your models here.

class House(models.Model):
    name = models.CharField(blank=True,max_length=255,unique=True)
    address = models.CharField(max_length=255,unique=True)
    room_size = models.DecimalField(max_digits=10,decimal_places=2)
    number_of_rooms = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField()
    last_updated = models.DateTimeField(auto_now=True)

    def save(self,*args,**kwargs):
        if not self.name:
            self.name = self.address
        super().save(*args,**kwargs)
    def __str__(self):
        return self.name

class Photo(models.Model):
    house = models.ForeignKey(House,related_name="images",on_delete=models.CASCADE)
    image = models.ImageField(upload_to="house images")

class Review(models.Model):
    house = models.ForeignKey(House,related_name="reviews",blank=True,on_delete=models.CASCADE)
    user = models.ForeignKey(UserAccount,related_name="reviews",blank=True,on_delete=models.CASCADE)
    rating = models.CharField(max_length=255)
    comment = models.TextField()
