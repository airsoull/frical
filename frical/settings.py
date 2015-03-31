# -*- coding: utf-8 -*-
import os

import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

ADMINS = (
    (os.getenv('ADMIN_NAME', 'example'), os.getenv('ADMIN_EMAIL', 'example@example.com')),
)

SECRET_KEY = 'im-8t^gkj*xi8qn@@wr9xswmaixyz%#_yj!=ix8=$l#*=eq*ic'

DEBUG = os.getenv('DEBUG', 'False') == 'True'
TEMPLATE_DEBUG = os.getenv('TEMPLATE_DEBUG', str(DEBUG)) == 'True'

ALLOWED_HOSTS = (os.getenv('ALLOWED_HOST', '*'),)
SITE_ID = os.getenv('SITE_ID', int(1))


AUTH_USER_MODEL = 'auth.User'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_extensions',
    'storages',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'frical.urls'

WSGI_APPLICATION = 'frical.wsgi.application'

DATABASES = {
    'default': dj_database_url.config(default='sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3'))
}

LANGUAGE_CODE = os.getenv('LANGUAGE_CODE', 'es-CL')
TIME_ZONE = os.getenv('TIME_ZONE', 'America/Santiago')
USE_I18N = True
USE_L10N = True
USE_TZ = True

gettext = lambda s: s
LANGUAGES = (
    ('en', gettext(u'English')),
    ('es', gettext(u'Español')),
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

STATIC_URL = os.getenv('STATIC_URL', '/static/')
MEDIA_ROOT = os.getenv('MEDIA_ROOT', os.path.join(BASE_DIR, 'media'))
MEDIA_URL = os.getenv('MEDIA_URL', '/media/')
STATIC_ROOT = os.getenv('STATIC_ROOT', os.path.join(BASE_DIR, 'static'))

EMAIL_BACKEND = os.getenv('EMAIL_BACKEND', 'django.core.mail.backends.console.EmailBackend')
EMAIL_HOST = os.getenv('EMAIL_HOST', 'localhost')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', '')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', '')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', 25))
EMAIL_SUBJECT_PREFIX = os.getenv('EMAIL_SUBJECT_PREFIX', '')
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS', 'False') == 'True'

AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
AWS_S3_SECURE_URLS = os.getenv('AWS_S3_SECURE_URLS', 'True') == 'True'
AWS_QUERYSTRING_AUTH = os.getenv('AWS_QUERYSTRING_AUTH', 'False') == 'True'

DEFAULT_FILE_STORAGE = os.getenv('DEFAULT_FILE_STORAGE', 'django.core.files.storage.FileSystemStorage')
STATICFILES_STORAGE = os.getenv('STATICFILES_STORAGE', 'django.contrib.staticfiles.storage.StaticFilesStorage')

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
