from .base import *

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["*"])
AUTH_PASSWORD_VALIDATORS = []
SECURE_SSL_REDIRECT = False