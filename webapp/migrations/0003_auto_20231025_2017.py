# Generated by Django 2.1.5 on 2023-10-25 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20231024_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='status',
            field=models.CharField(choices=[('Open', 'Open'), ('Closed', 'Closed'), ('Paused', 'Paused')], default='Open', max_length=50),
        ),
    ]