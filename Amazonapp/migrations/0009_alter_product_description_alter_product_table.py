# Generated by Django 5.0.7 on 2024-09-06 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Amazonapp', '0008_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterModelTable(
            name='product',
            table=None,
        ),
    ]
