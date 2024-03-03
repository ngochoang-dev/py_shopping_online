from typing import Any, Dict
from rest_framework.serializers import ModelSerializer
from .models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ('is_active', 'date_joined', 'password',)
        extra_kwargs = {
            'password': {'write_only': True}
        }

    
