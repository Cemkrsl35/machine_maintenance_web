from .base import *

STATIC_ROOT = "/var/cache/fk_motors/static"
MEDIA_ROOT = "/var/opt/fk_motors/media"

if env.bool("APPLY_EXTRA_SECURITY_SETTINGS", default=not DEBUG):
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_HSTS_SECONDS = 86400
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
