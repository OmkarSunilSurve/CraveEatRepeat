# Generated by Django 2.1.5 on 2023-10-27 05:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_auto_20231027_0100'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
