"""
Default ChatterBot settings for Django.
"""
from django.conf import settings
from core import constants


CHATTERBOT_SETTINGS = getattr(settings, 'CHATTERBOT', {})

CHATTERBOT_DEFAULTS = {
    'name': 'ChatterBot',
    'storage_adapter': 'core.storage.DjangoStorageAdapter',
    'django_app_name': constants.DEFAULT_DJANGO_APP_NAME
}

CHATTERBOT = CHATTERBOT_DEFAULTS.copy()
CHATTERBOT.update(CHATTERBOT_SETTINGS)
