from .base import *   #noqa

from .base import env

SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="S9ahuRl0FgVq_Nx0nm1vsbOXlWjw7RMUSY5TJHAiMUTXCg_WYv8",
    )


##   python3 -c "import secrets; print(secrets.token_urlsafe(38))"


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#ALLOWED_HOSTS = []

CSRF_TRUSTED_ORIGINS = ["http://localhost:8080"]