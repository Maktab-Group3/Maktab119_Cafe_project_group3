from django.contrib import admin
from .models import Order, OrderDetail, Receipt

# نمایش جزئیات سفارش داخل سفارش اصلی
class OrderDetailInline(admin.TabularInline):  # یا از StackedInline استفاده کن
    model = OrderDetail
    extra = 0  # جلوگیری از نمایش فیلد اضافی
    readonly_fields = ('item_name', 'quantity', 'item_price')  # جلوگیری از تغییر جزئیات سفارش در ادمین

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'table', 'payment_status', 'status', 'take_a_way', 'total_price')
    list_filter = ('payment_status', 'status', 'take_a_way')
    search_fields = ('id', 'table__name')
    inlines = [OrderDetailInline]  # اضافه کردن جزئیات سفارش به داخل سفارش
    fields = ('table', 'payment_status', 'status', 'take_a_way')  # فیلدهای قابل تغییر در ادمین

# class ReceiptAdmin(admin.ModelAdmin):
#     list_display = ('id', 'order', 'total_price', 'is_refunded','status_R')  
#     search_fields = ['id', 'order','status_R']
#     list_filter = ('status_R',)
#     fieldsets = [
#         ('Orders', {'fields': ['order']}),  
#         ('Total Price', {'fields': ['total_price']}),  
#         ('Refund Status', {'fields': ['is_refunded']}), 
#         ('Status Receipt' , {'fields': ['status_R']}), 
#     ]
    
# admin.site.register(Receipt, ReceiptAdmin) 

admin.site.register(Receipt)