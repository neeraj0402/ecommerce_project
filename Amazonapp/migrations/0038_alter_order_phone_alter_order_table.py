# Generated by Django 5.0.7 on 2024-09-09 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Amazonapp', '0037_alter_order_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(blank=True, default=None, max_length=10),
        ),
        migrations.AlterModelTable(
            name='order',
            table=None,
        ),
    ]