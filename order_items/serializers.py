from rest_framework.serializers import Serializer
from .models import OrderItem

class OrderItemSerializer(Serializer):
    class Meta:
        models = OrderItem
        fields = ["order_item_id","order_id","product_id","quantity","unit_price"]