# Generated by Django 5.0.7 on 2024-09-12 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Amazonapp', '0081_alter_order_address'),
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