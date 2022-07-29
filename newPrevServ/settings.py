"""
Django settings for newPrevServ project.

Generated by 'django-admin startproject' using Django 4.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
from pathlib import Path
from dotenv import load_dotenv
from os import getenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
from datasource.getResources import getDatabase, getEmailServer, getLoggingPsd
from utils.enums.conexoes import TipoConexao

# Carregando a SECRET_KEY das variáveis de ambiente
pathEnvVars = Path('.') / '.env'
if not pathEnvVars.is_file():
    print(f'{pathEnvVars.absolute()=}')
    raise Exception('Não foi possível encontrar o arquivo com as variáveis de ambiente.')
else:
    load_dotenv(pathEnvVars.absolute())

BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = getenv('SECRET_KEY', '')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition
INSTALLED_APPS = [
    # Django framework
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Django REST framework
    'django_filters',
    'drf_yasg',
    'rest_framework',

    # Meus apps
    'apps.advogado',
    'apps.escritorio',
    'apps.ferramentas',
    'apps.informacoes',
    'apps.newMails',
    'apps.sincron',
    'apps.gerenciamento',
]

REST_FRAMEWORK = {
    "DATE_INPUT_FORMATS": ["%Y-%m-%d"],
    "DATETIME_FORMAT": "%Y-%m-%d",
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'newPrevServ.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'newPrevServ.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = getDatabase(TipoConexao.hearthstone)


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

# STATIC_URL = '/static/'
STATIC_URL = os.path.join(BASE_DIR, 'static/')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static/')]
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'newPrevServ/static')]


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

AUTH_USER_MODEL = 'escritorio.Escritorio'

# Messages
from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: 'error',
    messages.SUCCESS: 'success',
    messages.INFO: 'info',
}

MESSAGE_STORAGE = "django.contrib.messages.storage.cookie.CookieStorage"

# Email
emailConfig: dict = getEmailServer()

EMAIL_HOST = emailConfig['emailHost']
EMAIL_PORT = emailConfig['port']
EMAIL_HOST_USER = emailConfig['emailHostUser']
EMAIL_HOST_PASSWORD = emailConfig['emailHostPassword']
SERVER_EMAIL = emailConfig['serverEmail']
EMAIL_USE_TLS = emailConfig['emailUseTls']
EMAIL_USE_SSL = emailConfig['emailUseSsl']

# LOGS
from logging import INFO
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from sentry_sdk.integrations.logging import LoggingIntegration

sentryLogging = LoggingIntegration(
    level=INFO,
    event_level=INFO
)

sentry_sdk.init(
    dsn=getLoggingPsd(),
    integrations=[sentryLogging, DjangoIntegration()],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)

from logs.newLoggin import NewLogging
logs = NewLogging()
