from .base import *

DATABASES = {
    "default": {
        "ENGINE": env("POSTGRES_ENGINE"),
        "NAME": env("POSTGRES_DB"),
        "USER": env("POSTGRES_USER"),
        "PASSWORD": env("POSTGRES_PASSWORD"),
        "HOST": env("PG_HOST"),
        "PORT": env("PG_PORT"),
    }
}

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# EMAIL_BACKEND = 'djcelery_email.backends.CeleryEmailBackend'  #After settings celery
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_PORT = env("EMAIL_PORT")
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
DEFAULT_FROM_EMAIL = "info@bangrealestate.com"
DOMAIN = env("DOMAIN")
SITE_NAME = "Real Estate"


#CELERY SETTINGS

# CELERY_BROKER_URL = env("CELERY_BROKER")
# CELERY_RESULT_BACKEND = env("CELERY_BACKEND")
# CELERY_TIMEZONE = "Asia/Ho_Chi_Minh"


# EMAIL_TIMEOUT
# EMAIL_SSL_KEYFILE
# EMAIL_SSL_CERTFILE