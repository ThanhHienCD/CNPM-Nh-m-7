# Generated by Django 5.1.4 on 2025-01-09 07:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppAuctionItem', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lot',
            name='year_published',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 9, 14, 51, 34, 286205)),
        ),
    ]