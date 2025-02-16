from django.core.validators import RegexValidator
from django.contrib.auth.hashers import make_password
from menu_items.models import MenuItem
from django.db import models
from orders.models import TimeStampeMixin
# Create your models here




phone_number_validator = RegexValidator(
    regex=r'^(\+98|0)?9\d{10}$',
    message="Phone number must be a valid Iranian phone number. like 0912******* or +98 912*******",
)

birth_date_validator = RegexValidator(
regex=r'^(19|20)\d{2}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$',
message="Enter a valid birth date in the format YYYY-MM-DD."
)

alpha_validator =RegexValidator(
    regex=r'^[A-Za-zآ-ی]{2,}$',
    message='Name must contain only English and Persian alphabets'
    )

# class User(models.Model):
#     first_name = models.CharField(max_length=100, validators=[alpha_validator])
#     last_name = models.CharField(max_length=100,validators=[alpha_validator])
#     phone_number = models.CharField(max_length=11 , unique=True, validators=[phone_number_validator])
#     email = models.EmailField(unique=True)
#     password = models.TextField()
#     birthday = models.DateField(auto_now_add=True, validators=[birth_date_validator])
   
#     def __str__(self):
#         return f"{self.first_name}  {self.last_name} "


