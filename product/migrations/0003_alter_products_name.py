# Generated by Django 5.0.7 on 2024-07-16 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_products_available_for_sale'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
