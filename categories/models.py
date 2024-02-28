from django.db import models

# Create your models here.
class Category(models.Model):
    class Meta:
        db_table = 'categories'

    category_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=255)

    def __str__(self) -> str:
        return super().__str__()