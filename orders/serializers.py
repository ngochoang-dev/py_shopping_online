from rest_framework.serializers import Serializer
from orders.models import Order

class OrderSerializer(Serializer):
    class Meta:
        model = Order
        fields = ["order_id","user_id","order_date","total_amount","status"]