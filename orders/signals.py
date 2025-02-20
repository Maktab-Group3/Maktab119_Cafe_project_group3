from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from .models import Order, Receipt

@receiver(post_save, sender=Order)
def create_receipt_for_completed_order(sender, instance, created, **kwargs):
    if instance.status == 'Delivered' and instance.payment_status == 'Successful' and not hasattr(instance, 'receipt'):
        if not hasattr(instance, 'receipt'):
            receipt = Receipt.objects.create(
                order=instance,
                total_price=float(instance.discounted_price),  
                original_price=float(instance.total_price),   
                user=instance.user,  
            )