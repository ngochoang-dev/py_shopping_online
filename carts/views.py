from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions 

from .models import Cart
from .serializers import CartSerializer
class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        request.data._mutable = True
        request.data['user_id'] = 8

        return super().create(request, *args, **kwargs)