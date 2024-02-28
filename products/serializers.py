from rest_framework.serializers import Serializer
from .models import Product

class ProductSerializer(Serializer):
    class Meta:
        model = Product
        fields = ["product_id","name","description","price","quantity"]