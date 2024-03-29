from django.contrib import admin
from .models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ("user_id", "username", "email", "phone", "is_staff", "is_superuser",)

admin.site.register(User, UserAdmin)