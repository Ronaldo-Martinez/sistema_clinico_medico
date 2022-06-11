"""
ASGI config for sistema_clinico_medico project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""
import django
django.setup()
import os
from django.urls import re_path
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack
from modulo_expediente.consumers import ColaExpedienteConsumer
from modulo_laboratorio.consumers import ColaLaboratorioConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sistema_clinico_medico.settings')

application = ProtocolTypeRouter({
        'http':get_asgi_application(),
        'https':get_asgi_application(),
        'websocket':AuthMiddlewareStack(
                URLRouter([
                        re_path(r'ws/laboratorio/cola/',ColaLaboratorioConsumer.as_asgi()),
                        re_path(r'ws/expediente/cola/',ColaExpedienteConsumer.as_asgi())
                ])
        )
})

