from django.contrib import admin
from .models import User

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    listdisplay = ['firstname', 'lastname', 'phonenumber', 'email', 'birthday']
    searchfields ='phone_number', 'email'
    ordering = 'first_name', 'last_name', 'phonenumber', 'email', 'birthday'


admin.site.register(User, UserAdmin)