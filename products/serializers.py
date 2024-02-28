from rest_framework.serializers import ModelSerializer, StringRelatedField
from .models import Product
from categories.serializers import CategorySerializer
class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_id' ,'name' ,'description' ,'price' ,'quantity',]