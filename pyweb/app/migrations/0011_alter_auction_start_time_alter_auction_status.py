# Generated by Django 5.1.4 on 2025-01-13 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_product_auction_alter_auction_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='auction',
            name='status',
            field=models.CharField(blank=True, choices=[('dang_dien_ra', 'Đang diễn ra'), ('sap_dien_ra', 'Sắp diễn ra'), ('ket_thuc', 'Kết thúc')], max_length=50, null=True),
        ),
    ]
