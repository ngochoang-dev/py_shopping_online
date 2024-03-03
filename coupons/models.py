from decimal import Decimal
from django.db import models
from users.models import User

from django.core.validators import MinValueValidator, MaxValueValidator
        
PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)]


class Coupon(models.Model):
    coupon_id= models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    code = models.CharField(max_length=100, null=False, blank=False) 
    discount = models.DecimalField(max_digits=3, decimal_places=0, default=Decimal(0), validators=PERCENTAGE_VALIDATOR, blank=False)
    exp = models.DateTimeField(null=False, blank=False)
    amount = models.IntegerField(null=False, blank=False)

    def __init__(self):
        return self.code
