# Generated by Django 5.1.2 on 2024-10-13 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0025_remove_category_sub_category_category_parents'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='expiry_date',
        ),
    ]