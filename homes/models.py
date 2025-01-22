from django.db import models
from src.db_utis import TimeStampedMixin

# Create your models here.


class Poll(TimeStampedMixin):
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    message = models.TextField()
    


    def __str__(self):
        return f"name:{self.name},email:{self.email}"