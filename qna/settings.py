"""
Django settings for qna project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SETTINGS_DIR = os.path.dirname(__file__)
PROJECT_PATH = os.path.join(SETTINGS_DIR, os.pardir)
PROJECT_PATH = os.path.abspath(PROJECT_PATH)
TEMPLATE_PATH = os.path.join(PROJECT_PATH, 'templates')



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'e(8vejalc#+x575!l*qm01h=t&$)v=hc74t5xp=&77q#_93$hp'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'base',
    'contents',
    'etests',
    'messaging',
)

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'qna.middleware.AutoLogout',
)

ROOT_URLCONF = 'qna.urls'

WSGI_APPLICATION = 'qna.wsgi.application'

SITE_ID = 1

AUTO_LOGOUT_DELAY=10

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LOCALE_PATHS = (os.path.join(BASE_DIR, 'locale'),)
LANGUAGE_CODE = 'en-us'

_ = lambda s: s
LANGUAGES = (
    ('mr', _('Marathi')),
    ('en', _('English')),
    ('hi', _('Hindi')),
    ('gu', _('Gujrati')),
)

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_PATH = os.path.join(BASE_DIR,'static')
#STATIC_ROOT = os.path.join(BASE_DIR,'static')
STATIC_URL = '/static/'

## Commented for Grappelli
#
STATICFILES_DIRS = (
    STATIC_PATH,
)


TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    TEMPLATE_PATH,
)

CRISPY_TEMPLATE_PACK = 'bootstrap3'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')


PASSWORD_HASHERS = (
'django.contrib.auth.hashers.PBKDF2PasswordHasher',
'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.request",
    "django.contrib.auth.context_processors.auth",
)