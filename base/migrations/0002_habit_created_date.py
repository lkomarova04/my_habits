# Generated by Django 3.2.5 on 2021-12-08 15:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
