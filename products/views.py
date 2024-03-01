from rest_framework.viewsets import  ModelViewSet
from rest_framework.decorators import action

from .models import Product
from .serializers import ProductSerializer

class ProductListView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer