# Generated by Django 4.2.6 on 2023-11-03 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.CharField(max_length=255)),
                ('current_status', models.CharField(choices=[('Checked In', 'Checked In'), ('Checked Out & Clean', 'Checked Out & Clean'), ('Checked Out', 'Checked Out')], max_length=255)),
            ],
        ),
    ]
