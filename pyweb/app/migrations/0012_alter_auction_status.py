# Generated by Django 5.1.4 on 2025-01-13 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_auction_start_time_alter_auction_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='status',
            field=models.CharField(blank=True, choices=[('ongoing', 'Đang diễn ra'), ('upcoming', 'Sắp diễn ra'), ('ended', 'Kết thúc')], max_length=50, null=True),
        ),
    ]
