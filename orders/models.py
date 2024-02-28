from django.db import models
from users.models import User

STATUSES = (
        ('PENDING', 'Pending'),
        ('PROCESSING', 'Processing'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    )

# Create your models here.
class Order(models.Model):
    class Meta:
        db_table = 'orders'

    order_id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=255, choices=STATUSES)

    def __str__(self) -> str:
        return super().__str__()
    