# Generated by Django 5.0.7 on 2024-09-09 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Amazonapp', '0016_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.IntegerField(blank=True, default='', max_length=10),
        ),
    ]
