# Generated by Django 5.0.7 on 2024-09-10 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Amazonapp', '0073_alter_order_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]