# Generated by Django 5.1.1 on 2024-09-24 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentschedule',
            name='keyword_difficulty',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='contentschedule',
            name='traffic_volume',
            field=models.PositiveIntegerField(default=0),
        ),
    ]