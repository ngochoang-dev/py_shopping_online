from rest_framework.serializers import ModelSerializer
from django.contrib.auth.hashers import make_password

from .models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ('is_active', 'date_joined')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)
