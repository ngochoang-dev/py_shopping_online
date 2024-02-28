from rest_framework.serializers import Serializer
from .models import User

class UserSerializer(Serializer):
    class Meta:
        model = User
        fields = ["user_id", "username", "email", "phone"]