from django.db import models

# Create your models here.
class Polls(models.Model):
    name = models.CharField(max_length=30,null=False)
    email = models.EmailField(unique=True,null=False)
    message = models.TextField(max_length=250)