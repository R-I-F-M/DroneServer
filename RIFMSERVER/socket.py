from django.urls import path
from .consumers import DroneConsumer


websocket_urlpatterns =[

    path('ws/wsc/',DroneConsumer.as_asgi())
]