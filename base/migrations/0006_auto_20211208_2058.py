# Generated by Django 3.2.5 on 2021-12-08 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_rename_name_habit_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='Fri',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='habit',
            name='Mon',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='habit',
            name='Sat',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='habit',
            name='Sun',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='habit',
            name='Thu',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='habit',
            name='Tue',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='habit',
            name='Wed',
            field=models.BooleanField(default=False),
        ),
    ]
