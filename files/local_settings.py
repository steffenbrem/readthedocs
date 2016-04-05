import os

from .base import SITE_ROOT

DATABASES = {
    'default': {
        'ENGINE': os.getenv('DJANGO_DB_ENGINE', 'django.db.backends.sqlite3'),
        'NAME': os.getenv('DJANGO_DB_NAME', os.path.join(SITE_ROOT, 'dev.db')),
        'USER': os.getenv('DJANGO_DB_USER', 'postgres'),  # Not used with sqlite3.
        'PASSWORD': os.getenv('DJANGO_DB_PASSWORD', ''),
        'HOST': os.getenv('DJANGO_DB_HOST', 'postgres'),
        'PORT': os.getenv('DJANGO_DB_PORT', ''),
    }
}

USE_SUBDOMAIN = True
SLUMBER_USERNAME = 'docbuilder'
SLUMBER_PASSWORD = os.getenv('RTD_SLUMBER_PASSWORD', 'docbuilder')
PRODUCTION_DOMAIN = 'docs.shopblender.nl'
SECRET_KEY = 'changemeplease'
