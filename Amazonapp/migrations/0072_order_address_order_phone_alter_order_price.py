# Generated by Django 5.0.7 on 2024-09-10 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Amazonapp', '0071_remove_order_phone_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
