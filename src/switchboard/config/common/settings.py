"""
.. module:: switchboard.config.common.settings
   :synopsis: Common project settings, applies to all environments.
"""

from os import environ
from os.path import abspath, join, dirname

ALLOWED_HOSTS = [

]


""" Paths """
SITE_ROOT = abspath(join(dirname(__file__), '..', '..'))
PROJECT_ROOT = abspath(join(dirname(__file__), '..', '..'))
MEDIA_ROOT = join(PROJECT_ROOT, '..', '..', 'media')
STATICFILES_DIRS = [
    join(PROJECT_ROOT, 'public'), ]
LOG_ROOT = join(PROJECT_ROOT, 'logs')

""" Urls """
STATIC_URL = '/s/'
MEDIA_URL = '/m/'
ROOT_URLCONF = 'switchboard.urls'

""" Secret Key & Site ID """
SITE_ID = 1
SECRET_KEY = '*sx8l%vo7@-+lzqw@_yi)3u1hooe&so^e^0w1n0@o!v(p_3n#u'

""" Location """
TIME_ZONE = 'Europe/London'
USE_I18N = True
USE_L10N = True

""" Templates """
TEMPLATE_DIRS = [
    join(PROJECT_ROOT, 'templates'),
    join(PROJECT_ROOT, 'twiliorouter', 'templates')
]

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
TEMPLATE_CONTEXT_PROCESSORS = (
    # Common django context processors
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    # Custom project context processprs
    'switchboard.context_processors.domain',
)

""" Middleware """
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

""" Installed Applications """
INSTALLED_APPS = [
    # Admin Bootstrapped
    'django_admin_bootstrapped',
    # Django Apps
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    # Third Party Apps here
    'south',
    'django_twilio',
    # Project Apps here
    'switchboard',
    'switchboard.twiliorouter',
]


""" Test Suite """
NOSE_ARGS = [
    '--include=^(can|it|ensure|must|should|specs?|examples?)',
    '--with-spec',
    '--spec-color',
    '-s',
    '--with-coverage',
    '--cover-erase',
    '--cover-package=voting']
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

""" Session config """
SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

""" Twilio account settings """
TWILIO_ACCOUNT_SID = 'AC4a15c1d0a08d0807e6a64d4228a65362'
TWILIO_AUTH_TOKEN = '490405cfaeccf2fccb1e2728bc9017b6'
DJANGO_TWILIO_FORGERY_PROTECTION = True
