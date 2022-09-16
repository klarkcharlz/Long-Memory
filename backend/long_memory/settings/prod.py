import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from .common import *


config = dotenv_values(".env")

DEBUG = False

sentry_sdk.init(
    dsn=config['SENTRY_DSN'],
    integrations=[DjangoIntegration()],
    traces_sample_rate=1.0,
    send_default_pii=True,
)
