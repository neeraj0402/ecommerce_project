# Generated by Django 5.0.7 on 2024-09-09 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Amazonapp', '0063_order_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='price',
            field=models.IntegerField(default=None),
        ),
    ]
