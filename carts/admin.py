from django.contrib import admin
from .models import Cart

# Register your models here.
class CartAdmin(admin.ModelAdmin):
    list_display = ("cart_id","user_id","product","quantity","date_added")

admin.site.register(Cart, CartAdmin)