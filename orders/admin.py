from django.contrib import admin
from .models import Receipt

class ReceiptAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'total_price', 'is_refunded','status_R')  
    search_fields = ['id', 'order','status_R']
    list_filter = ('status_R',)
    fieldsets = [
        ('Orders', {'fields': ['order']}),  
        ('Total Price', {'fields': ['total_price']}),  
        ('Refund Status', {'fields': ['is_refunded']}), 
        ('Status Receipt' , {'fields': ['status_R']}), 
    ]
    
   
      



admin.site.register(Receipt, ReceiptAdmin) 
