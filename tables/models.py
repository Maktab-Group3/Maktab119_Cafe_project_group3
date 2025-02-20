from django.db import models
# from orders.models import Order

class Table(models.Model):
    POSITION_CHOICES = [
        ('window', 'Near Window'),
        ('door', 'Near Door'),
        ('corner', 'In Corner'),
        ('center', 'Center of Cafe'),
        ('outdoor', 'Outdoor'),
        ('bar', 'Near Bar'),
        ('private', 'Private Room')
    ]

    table_number = models.PositiveIntegerField()
    cafe_space_position = models.CharField(max_length=20, choices=POSITION_CHOICES)

    def __str__(self):
        return f"Table {self.table_number} - {self.get_cafe_space_position_display()}"