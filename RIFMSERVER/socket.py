# socket.py

from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from .consumers import consumers

websocket_urlpatterns = [
    path('ws/drone/', consumers.DroneConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    'websocket': URLRouter(
        websocket_urlpatterns
    ),
})
