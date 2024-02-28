from rest_framework.serializers import ModelSerializer
from orders.models import Order

class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ["order_id","user_id","order_date","total_amount","status"]