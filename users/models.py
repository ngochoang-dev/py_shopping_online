from django.db import models
from django.contrib.auth.models import  AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    username = None
    user_id = models.BigAutoField(primary_key=True)
    phone = models.CharField(max_length=11, blank=True)
    avatar = models.CharField(max_length=255, blank=True)
    email = models.EmailField(_("email address"), blank=False, null=False, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'