from django.db import models
import uuid

class Product(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.CharField(max_length=255)
    stock = models.PositiveIntegerField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    
