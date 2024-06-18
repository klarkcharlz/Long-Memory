import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from .common import *


config = dotenv_values(".env")

DEBUG = False
SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
MEDIA_URL = 'https://longmemory.ru/media/'
STATIC_URL = 'https://longmemory.ru/static/'
SESSION_COOKIE_SAMESITE = 'Lax'  # Или 'Strict', в зависимости от ваших требований
CSRF_COOKIE_SAMESITE = 'Lax'
    
sentry_sdk.init(
    dsn=config['SENTRY_DSN'],
    integrations=[DjangoIntegration()],
    traces_sample_rate=1.0,
    send_default_pii=True,
)
