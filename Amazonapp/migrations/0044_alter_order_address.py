# Generated by Django 5.0.7 on 2024-09-09 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Amazonapp', '0043_alter_order_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(blank=None, default=None, max_length=50),
        ),
    ]