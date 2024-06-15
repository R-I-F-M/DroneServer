"""
ASGI config for drone_server project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from .socket import websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'drone_server.settings')

application = get_asgi_application()

socket_application  = ProtocolTypeRouter({
    "http": application,
    "websocket": URLRouter(
        websocket_urlpatterns
    )
    # Just HTTP for now. (We can add other protocols later.)
})