from rest_framework.viewsets import  ModelViewSet, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from .models import Product
from .serializers import ProductSerializer

class PermissionCustomer:
    def has_permission(self, request, view):
        return True

class ProductListView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [PermissionCustomer]

    @action(methods=['get'], detail=True, permission_classes=[permissions.IsAdminUser])
    def get_desc(self, request, pk=None):
        try:
            queryset =  Product.objects.get(pk=pk)
            ser = ProductSerializer(queryset).data.get("description")
    
            return Response(ser, status=200)
        except Product.DoesNotExist:
            return Response({"message": "Not found"}, status=404)
        