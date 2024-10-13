
from django.db import models
from versatileimagefield.fields import VersatileImageField




class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    # sub_category = models.ManyToManyField('self', blank=True, symmetrical=False)
    parents = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(null=True)
    expiry_date = models.DateField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    photo = VersatileImageField(
        'image',
        upload_to='products/',
        null=True,
        blank=True,)

    def __str__(self):
        photo_exist=self.photo if self.photo else None
        return f'{self.name}, {self.price}, {self.category.name}, {photo_exist}'
