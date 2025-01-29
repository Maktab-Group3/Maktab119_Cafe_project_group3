from django.db import models

# Create your models here.
# class Poll(models.Model):
#     name = models.CharField(max_length=30)
#     email = models.EmailField(unique=True)
#     message = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)


#     def __str__(self):
#         return f"name:{self.name},email:{self.email}"
class Category(models.Model):
    
    name = models.CharField(max_length=35)   
    
    def __str__(self):
        return f"{self.name}"
    

class MenuItem(models.Model):
    name = models.CharField(max_length=100)

    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


class CartItem(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)

    items = models.ManyToManyField(MenuItem)

    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)    