from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'name', 'description', 'price', 'quantity', 'category_id')

admin.site.register(Product, ProductAdmin)