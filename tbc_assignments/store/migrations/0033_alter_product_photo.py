# Generated by Django 5.1.1 on 2024-10-16 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0032_alter_product_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='image'),
        ),
    ]