from django.db import models
from users.models import User
from products.models import Product

# Create your models here.
class Cart(models.Model):
    class Meta:
        db_table = 'carts'

    cart_id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return super().__str__()