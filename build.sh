#!/usr/bin/env bash
# exit on error
set -o errexit

# poetry install
pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

# Nombre de usuario, correo electrónico y contraseña para el superusuario
username="admin"
email="admin@example.com"
password="admin_password"

# Verifica si el superusuario ya existe
if ! python -c "from django.contrib.auth.models import User; print(User.objects.filter(username='$username').exists())"; then
    # Crea un nuevo superusuario
    echo "from django.contrib.auth.models import User; User.objects.create_superuser('$username', '$email', '$password')" | python manage.py shell

    echo "Superusuario creado con éxito!"
else
    echo "El superusuario ya existe."
fi