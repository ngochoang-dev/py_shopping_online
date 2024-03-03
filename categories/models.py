from django.db import models


class Category(models.Model):
    category_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'{self.name}'