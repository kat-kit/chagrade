"""
Django settings for chagrade project.

Generated by 'django-admin startproject' using Django 1.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
import dj_database_url
from decouple import config

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CHAGRADE_BASE_DIR = os.path.dirname(BASE_DIR)

SITE_DOMAIN = os.environ.get('SITE_DOMAIN', 'http://localhost')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'n2q(v$c6@o^9j^0f=$lwwr7%p2xrjt$_6^4l&+6em^m^5l9y&4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Third Party
    'django_extensions',
    'social_django',
    'rest_framework',
    'drf_yasg',
    'oauth2_provider',
    'storages',
    # Our Apps
    'apps.profiles',
    'apps.klasses',
    'apps.homework',
    'apps.groups',
    'apps.api',
    'apps.factory',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

# STATIC_ROOT = '/static/'
STATICFILES_DIRS = (
    os.path.join(CHAGRADE_BASE_DIR, 'static'),
)
# STATIC_ROOT = os.path.join(CHAGRADE_BASE_DIR, 'static')
#
STATIC_ROOT = os.path.join(CHAGRADE_BASE_DIR, 'staticfiles')
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

ROOT_URLCONF = 'chagrade.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(CHAGRADE_BASE_DIR, 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'apps.profiles.context_processors.password_reset_requests_processor'
            ],
        },
    },
]

WSGI_APPLICATION = 'chagrade.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

# Heroku DB Settings
if os.environ.get('DATABASE_URL'):
    DATABASES = {
        'default': dj_database_url.config(default=config('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ.get('DB_NAME', 'chagrade_website'),
            'USER': os.environ.get('DB_USER', 'postgres'),
            'PASSWORD': os.environ.get('DB_PASSWORD', ''),
            'HOST': os.environ.get('DB_HOST', 'postgres'),
            'PORT': os.environ.get('DB_PORT', '5432'),
        }
    }


AUTH_USER_MODEL = 'profiles.ChaUser'

AUTHENTICATION_BACKENDS = (
    # "apps.chahub_auth.oauth_backends.ChahubOAuth2",
    "django.contrib.auth.backends.ModelBackend",
    "apps.profiles.auth_backends.EmailBackend",
    "social_core.backends.github.GithubOAuth2",

)

# =========================================================================
# Social Auth
# =========================================================================

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.social_auth.associate_user',
    'apps.profiles.pipeline.user_details',
)

# Generic
SOCIAL_AUTH_STRATEGY = 'social_django.strategy.DjangoStrategy'
SOCIAL_AUTH_STORAGE = 'social_django.models.DjangoStorage'
SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['username', 'first_name', 'email']

SOCIAL_AUTH_CHAHUB_KEY = os.environ.get('SOCIAL_AUTH_CODALAB_KEY')
SOCIAL_AUTH_CHAHUB_SECRET = os.environ.get('SOCIAL_AUTH_CODALAB_SECRET')

SOCIAL_AUTH_CHAHUB_BASE_URL = os.environ.get('SOCIAL_AUTH_CHAHUB_BASE_URL', 'https://chahub.org')

SOCIAL_AUTH_LOGIN_REDIRECT_URL = 'index'
SOCIAL_AUTH_LOGIN_URL = 'profiles:login'
# SOCIAL_AUTH_NEW_USER_REDIRECT_URL = 'profiles:set_password'
SOCIAL_AUTH_NEW_USER_REDIRECT_URL = 'index'
# SOCIAL_AUTH_NEW_ASSOCIATION_REDIRECT_URL = 'profiles:set_password'
SOCIAL_AUTH_NEW_ASSOCIATION_REDIRECT_URL = 'index'
SOCIAL_AUTH_DISCONNECT_REDIRECT_URL = 'index'

LOGIN_URL = 'profiles:login'
LOGIN_REDIRECT_URL = 'index'

# Github
SOCIAL_AUTH_GITHUB_KEY = os.environ.get('SOCIAL_AUTH_GITHUB_KEY')
SOCIAL_AUTH_GITHUB_SECRET = os.environ.get('SOCIAL_AUTH_GITHUB_SECRET')
SOCIAL_AUTH_GITHUB_SCOPE = ['user']

# User Models
# SOCIAL_AUTH_USER_MODEL = 'authenz.ClUser'
SOCIAL_AUTH_USER_MODEL = 'profiles.ChaUser'

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# =============================================================================
# SSL
# =============================================================================
if os.environ.get('USE_SSL'):
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
else:
    # Allows us to use with django-oauth-toolkit on localhost sans https
    SESSION_COOKIE_SECURE = False

# ============================================================================
# Celery
# ============================================================================
BROKER_URL = os.environ.get("BROKER_URL")
# CELERY_RESULT_BACKEND = 'djcelery.backends.database:DatabaseBackend'


# =============================================================================
# DRF
# =============================================================================
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.URLPathVersioning',
    'DEFAULT_VERSION': 'v1',

    # Why did I add this?
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    # 'PAGE_SIZE': 10,
}
REST_FRAMEWORK_EXTENSIONS = {
    'DEFAULT_CACHE_RESPONSE_TIMEOUT': 60 * 15
}

FILE_UPLOAD_HANDLERS = ["django.core.files.uploadhandler.TemporaryFileUploadHandler", ]

# =============================================================================
# S3 Storage
# =============================================================================

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_LOCATION = os.environ.get('AWS_LOCATION', 'chagrade')
# AWS_DEFAULT_ACL = None

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# =============================================================================
# Email
# =============================================================================

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_HOST = 'host.docker.internal'

SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')
SENDGRID_FROM_EMAIL = os.environ.get('SENDGRID_FROM_EMAIL')

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = os.environ.get('SENDGRID_USERNAME')
EMAIL_HOST_PASSWORD = os.environ.get('SENDGRID_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# =============================================================================
# Custom
# =============================================================================

ALLOWED_SUBMISSION_DOMAINS = [
    'github.com'
]
