# Generated by Django 5.0.7 on 2024-09-09 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Amazonapp', '0058_order_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.IntegerField(default=None),
        ),
    ]