# Generated by Django 3.1.4 on 2020-12-17 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0006_auto_20201218_0155'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('Complete', 'Incomplete')], max_length=50, null=True),
        ),
    ]