# Generated by Django 4.2.6 on 2023-11-03 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hms', '0003_booking_delete_bookings'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='coupon',
            field=models.CharField(default='Coupon', max_length=100),
        ),
    ]
