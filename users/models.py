from django.db import models

# Create your models here.
class User(models.Model):
    class Meta:
        db_table = 'users'

    user_id = models.BigAutoField(primary_key=True) 
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.BinaryField
    phone = models.CharField(max_length=11, unique=True)

    def __str__(self) -> str:
        return f'{self.username}'