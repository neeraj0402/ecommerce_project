# Generated by Django 5.0.7 on 2024-09-09 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Amazonapp', '0024_alter_order_address_alter_order_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(blank=True, default='1', max_length=50),
        ),
    ]