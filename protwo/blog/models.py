from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
class BlogPost(models.Model):
    content = models.CharField(max_length=1000)
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
