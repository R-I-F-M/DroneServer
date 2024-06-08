from django.db import models

class DroneServer(models.Model):
    title = models.CharField(max_length=50, default="RIFM Controllers")
    is_spraying_operation = models.CharField(max_length=50)
   
    is_home_setpoint = models.CharField(max_length=50)

    is_emergency_droneland = models.CharField(max_length=50)

    is_drone_connected = models.CharField(max_length=50)


    def __str__(self):
        return self.title
