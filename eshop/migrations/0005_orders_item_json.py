# Generated by Django 4.2.5 on 2023-09-29 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0004_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='item_json',
            field=models.CharField(default='', max_length=6000),
        ),
    ]
