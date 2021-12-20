from .base import *  # noqa
from .base import env

from django.utils.crypto import get_random_string

# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = get_random_string(50),

# DATABASES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR.joinpath('database.sqlite'),
    }
}

REST_FRAMEWORK['TEST_REQUEST_DEFAULT_FORMAT'] = 'json'
REST_FRAMEWORK['TEST_REQUEST_RENDERER_CLASSES'] = ['rest_framework.renderers.JSONRenderer']
