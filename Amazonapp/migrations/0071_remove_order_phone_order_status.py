# Generated by Django 5.0.7 on 2024-09-10 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Amazonapp', '0070_remove_order_status_order_phone_alter_order_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='phone',
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
