from rest_framework.serializers import ModelSerializer
from .models import OrderItem

class OrderItemSerializer(ModelSerializer):
    class Meta:
        models = OrderItem
        fields = ["order_item_id","order_id","product_id","quantity","unit_price"]