# Generated by Django 4.2.2 on 2023-06-16 05:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_category_image_alter_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='stock',
        ),
    ]
