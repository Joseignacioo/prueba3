# miapp/management/create_superuser.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Crea un superusuario automáticamente'

    def handle(self, *args, **options):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                'admin',
                'tu_correo@dominio.com',
                'Prueba3'
            )
            self.stdout.write(self.style.SUCCESS('Superusuario creado con éxito'))
        else:
            self.stdout.write(self.style.SUCCESS('El superusuario ya existe'))