# Generated by Django 3.1.4 on 2020-12-21 08:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0015_auto_20201221_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='create_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]