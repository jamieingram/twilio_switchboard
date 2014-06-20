"""
.. module:: switchboard.config.dev.settings
"""

from ..common.settings import *


""" Debugging (default True for development environment) """
DEBUG = True
TEMPLATE_DEBUG = DEBUG

""" Databases (default is mysql) """
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'switchboard',
        'USER': 'root',
        'PASSWORD': 'root',
    }
}

""" Use MD5 Password Hashing for Dev - Speeds things up """
PASSWORD_HASHERS = ['django.contrib.auth.hashers.MD5PasswordHasher']

""" So constance config vars can be exposed via django.conf.settings """
try:
    from constance import config
except ImportError:
    pass
else:
    try:
        THE_ANSWER_TO_EVERYTHING = config.THE_ANSWER_TO_EVERYTHING
    except:
        pass

DJANGO_TWILIO_FORGERY_PROTECTION = False
