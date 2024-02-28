from rest_framework.serializers import Serializer
from .models import Cart

class CartSerializer(Serializer):
    class Meta:
        model = Cart
        fields = ["cart_id","user_id","product","quantity","date_added"]