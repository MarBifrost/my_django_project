# Register your models here.
from django.apps import AppConfig

class OrderConfig(AppConfig):
    default_auto_field = 'django.db.models.AutoField'
    name = 'order'

    def ready(self):
        import order.signals



