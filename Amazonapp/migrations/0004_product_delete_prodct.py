# Generated by Django 5.0.7 on 2024-09-06 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Amazonapp', '0003_prodct_delete_amazon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('description', models.CharField(default='', max_length=200)),
                ('image', models.ImageField(upload_to='uploads/products/')),
            ],
            options={
                'db_table': 'Product',
            },
        ),
        migrations.DeleteModel(
            name='Prodct',
        ),
    ]
