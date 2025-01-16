# Generated by Django 5.1.4 on 2025-01-13 17:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_remove_auction_hour_end'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='auction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.auction'),
        ),
        migrations.AlterField(
            model_name='auction',
            name='status',
            field=models.CharField(blank=True, choices=[('ongoing', 'Đang diễn ra'), ('upcoming', 'Sắp diễn ra'), ('ended', 'Kết thúc')], max_length=50, null=True),
        ),
    ]
