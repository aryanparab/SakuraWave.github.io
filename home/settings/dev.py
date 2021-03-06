'''Use this for development'''
import config
from .base import *

ALLOWED_HOSTS = ["sakurawave.in" , '127.0.0.1',"sakurawave.github.io","sakurawave.herokuapp.com"]

DEBUG = False

WSGI_APPLICATION = 'home.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

CORS_ORIGIN_WHITELIST = (
    'http://localhost:3000',
)

# Stripe

# STRIPE_PUBLIC_KEY = config('STRIPE_TEST_PUBLIC_KEY')
# STRIPE_SECRET_KEY = config('STRIPE_TEST_SECRET_KEY')
