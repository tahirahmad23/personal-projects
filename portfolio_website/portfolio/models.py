from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    content = CKEditor5Field(config_name= "extends")  # This enables rich text editing
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
