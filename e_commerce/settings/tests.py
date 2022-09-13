"""
With these settings, tests run faster.
"""

from e_commerce.settings.settings import *

# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = False

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "",
    }
}