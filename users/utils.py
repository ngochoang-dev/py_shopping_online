from users.models import User
from rest_framework import permissions
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.exceptions import AuthenticationFailed

class IsStaff(permissions.BasePermission):
    def has_permission(self, request, view):
        token =  request.META.get('HTTP_AUTHORIZATION').split(' ')
        if not len(token):
            return AuthenticationFailed("You are not authorized to")
        if(token[0] != 'Bearer'):
            return AuthenticationFailed("Invalid Bearer token")
        if not token[1]:
            return AuthenticationFailed("You are not authorized to")
        
        user_id = AccessToken(token[1])['user_id']

        user = User.objects.get(pk=user_id)

        if not user.is_staff:
            return False

        return True