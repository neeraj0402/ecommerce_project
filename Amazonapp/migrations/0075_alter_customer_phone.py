# Generated by Django 5.0.7 on 2024-09-10 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Amazonapp', '0074_alter_order_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]