# Generated by Django 4.2 on 2023-07-10 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_product_options_remove_category_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='weight',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]
