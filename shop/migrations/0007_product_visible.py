# Generated by Django 4.2 on 2023-07-11 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_alter_product_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='visible',
            field=models.BooleanField(default=True),
        ),
    ]
