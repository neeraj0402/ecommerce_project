# Generated by Django 5.0.7 on 2024-09-09 07:45

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Amazonapp', '0033_delete_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('price', models.IntegerField()),
                ('address', models.CharField(blank=True, default='', max_length=100)),
                ('date', models.DateField(default=datetime.datetime.today)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Amazonapp.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Amazonapp.product')),
            ],
            options={
                'db_table': 'Order',
            },
        ),
    ]
