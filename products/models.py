from django.db import models
from categories.models import Category


class Product(models.Model):
    product_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=0) 
    quantity = models.IntegerField(null=False)
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.name}'