from rest_framework.serializers import ModelSerializer
from .models import Cart

class CartSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = ["cart_id", "user_id", "product", "quantity", "date_added"]
