import uuid

from django.db import models
from user.models import CustomUser

# Create your models here.
class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.CharField(max_length=50)
    quantity = models.IntegerField()
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    shipping_address = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} - {self.last_name}-{self.product}"


class UserCart(models.Model):
    user=models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}'s cart"
