from rest_framework.serializers import ModelSerializer
from .models import Product
class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_id' ,'name' ,'description' ,'price' ,'quantity', 'category']
