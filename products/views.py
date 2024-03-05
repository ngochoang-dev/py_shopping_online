from rest_framework.viewsets import mixins, GenericViewSet
from rest_framework.decorators import action
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer
from users.utils import IsStaff

class ProductListView(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]

    @action(methods=['POST'], permission_classes=[IsStaff], detail=False)
    def create_product(self, request):
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(methods=['POST'], permission_classes=[IsStaff], detail=True)
    def delete_product(self, request, pk):
        print(pk)
        try:
            product = Product.objects.get(pk=pk)
            product.delete()
            return Response({'message': 'Successfully'}, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({'message': 'Product doesn\'t exist'}, status=status.HTTP_400_BAD_REQUEST)
