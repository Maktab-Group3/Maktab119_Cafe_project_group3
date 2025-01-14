from django.db import models
from django.db import make_password
from menuitems.models import MenuItem
from django.core.validators import MinLengthValidator , RegexValidator
# Create your models here

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=11 , unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    birthday = models.DateField(auto_now_add=True)
    subscription_number = models.IntegerField(unique=True)

   
class Comment(models.Model):
    text = models.TextField(max_length=2000 )
    date_comment = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE , name="user")
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE , name="menu_item")