# Generated by Django 5.0.7 on 2024-07-16 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='available_for_sale',
            field=models.BooleanField(default=False),
        ),
    ]
