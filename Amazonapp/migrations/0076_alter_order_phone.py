# Generated by Django 5.0.7 on 2024-09-10 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Amazonapp', '0075_alter_customer_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.IntegerField(blank=True,default=0, null=True),
        ),
    ]