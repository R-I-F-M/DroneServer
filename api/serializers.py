from rest_framework import serializers
from .models import DroneServer

class ServerSerializers(serializers.ModelSerializer):
    class Meta:
        model = DroneServer
        fields = '__all__'
