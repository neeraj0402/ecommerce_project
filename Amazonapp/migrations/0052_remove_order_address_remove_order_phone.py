# Generated by Django 5.0.7 on 2024-09-09 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Amazonapp', '0051_alter_order_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='address',
        ),
        migrations.RemoveField(
            model_name='order',
            name='phone',
        ),
    ]