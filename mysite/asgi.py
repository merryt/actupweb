"""
ASGI config for mysite project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os


from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application


django_asgi_app = get_asgi_application()
# Initialize Django ASGI application early to ensure the AppRegistry
# is populated before importing code that may import ORM models.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

import shows.routing

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(URLRouter(shows.routing.websocket_urlpatterns))
    )
})


