from django.db.models.signals import post_save
from django.dispatch import receiver
from user.models import CustomUser
from order.models import UserCart

@receiver(post_save, sender=CustomUser)
def customer_cart(sender, instance, create, **kwargs):
    if create:
        UserCart.objects.create(user=instance)
