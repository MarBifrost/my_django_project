# Generated by Django 5.1.1 on 2024-10-10 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_product_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='parents',
            field=models.ManyToManyField(blank=True, to='store.product'),
        ),
    ]