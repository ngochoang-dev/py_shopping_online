from django.contrib import admin
from .models import OrderItem

# Register your models here.
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("order_item_id","order_id","product_id","quantity","unit_price")

admin.site.register(OrderItem, OrderItemAdmin)