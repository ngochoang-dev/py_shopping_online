from django.contrib import admin
from .models import Order

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ("order_id","user_id","order_date","total_amount","status")

admin.site.register(Order, OrderAdmin)