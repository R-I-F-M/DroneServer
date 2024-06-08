# Generated by Django 5.0.4 on 2024-04-27 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_droneserver_is_drone_disconnected_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='droneserver',
            name='is_drone_connected',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='droneserver',
            name='is_emergency_droneland',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='droneserver',
            name='is_home_setpoint',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='droneserver',
            name='is_spraying_operation',
            field=models.CharField(max_length=50),
        ),
    ]
