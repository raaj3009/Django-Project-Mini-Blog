from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    
class Contact(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField()
    address = models.CharField(max_length=150)
    message = models.TextField()