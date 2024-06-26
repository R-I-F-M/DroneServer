# Generated by Django 5.0.4 on 2024-04-26 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_droneserver_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='droneserver',
            name='is_drone_disconnected',
        ),
        migrations.RemoveField(
            model_name='droneserver',
            name='is_emergency_droneland_off',
        ),
        migrations.RemoveField(
            model_name='droneserver',
            name='is_home_setpoint_off',
        ),
        migrations.RemoveField(
            model_name='droneserver',
            name='is_spraying_operation_off',
        ),
        migrations.AlterField(
            model_name='droneserver',
            name='is_drone_connected',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='droneserver',
            name='is_emergency_droneland',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='droneserver',
            name='is_home_setpoint',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='droneserver',
            name='is_spraying_operation',
            field=models.BooleanField(default=False),
        ),
    ]
