# Generated by Django 2.1.5 on 2023-10-29 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_remove_order_delivery_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_status',
            field=models.IntegerField(default=0),
        ),
    ]