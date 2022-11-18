from django.contrib.auth.models import User
from django.db import models
from django.db.models.query import F

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=20, null=False)
    image = models.ImageField(upload_to='project/', null=False)
    description = models.CharField(max_length=200, null=True)
    
    created_at = models.DateField(auto_now_add=True, null=True)
    
    def __str__(self):
        return f'{self.pk} : {self.title}'