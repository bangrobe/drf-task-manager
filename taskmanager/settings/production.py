
import os
from .base import *


DEBUG = False

ADMINS = [
    ('Bang Nguyen', 'bangrobe@gmail.com'),
]

ALLOWED_HOSTS = ['*']
SECRET_KEY=os.environ.get('SECRET_KEY')
DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': os.environ.get('POSTGRES_DB'),
       'USER': os.environ.get('POSTGRES_USER'),
       'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
       'HOST': 'db',
       'PORT': 5432,
   }
}

# REDIS_URL = 'redis://cache:6379'
# CACHES['default']['LOCATION'] = REDIS_URL
# CHANNEL_LAYERS['default']['CONFIG']['hosts'] = [REDIS_URL]

# Security
# CSRF_COOKIE_SECURE = True
# SESSION_COOKIE_SECURE = True
# SECURE_SSL_REDIRECT = True

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# EMAIL_BACKEND = 'djcelery_email.backends.CeleryEmailBackend'  #After settings celery
EMAIL_HOST = os.environ.get("EMAIL_HOST")
EMAIL_PORT = os.environ.get("EMAIL_PORT")
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
DEFAULT_FROM_EMAIL = "info@taskmanager.com"
DOMAIN = os.environ.get("DOMAIN")
SITE_NAME = "Task Manager"

STATIC_ROOT = '/var/www/mysite/assets/'