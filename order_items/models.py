from django.db import models
from orders.models import Order
from products.models import Product

# Create your models here.
class OrderItem(models.Model):
    class Meta:
        db_table = 'order_items'

    order_item_id = models.BigAutoField(primary_key=True)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False)
    unit_price = models.CharField(max_length=50)

    def __str__(self) -> str:
        return super().__str__()