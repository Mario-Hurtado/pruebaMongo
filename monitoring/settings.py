"""
Django settings for monitoring project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'g#g&#%)vbrjq$j+x((1a(wrf_a*x%8#cays-+j^_j27=cv054l'

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
    'tendero',
    'tienda',
    'productoChiper',
    'productoPedido',
    'pedidos',
    'ventas',
    'productoVenta',
    'zonas',
    'reportes',
    'social_django'
]


LOGIN_URL = "/login/auth0"
LOGIN_REDIRECT_URL = "/autenticado/"
LOGOUT_REDIRECT_URL = "https://isis2503-mario-hurtado.auth0.com/v2/logout?returnTo=http%3A%2F%2F54.198.254.78:80"

SOCIAL_AUTH_TRAILING_SLASH = False # Remove end slash from routes
SOCIAL_AUTH_AUTH0_DOMAIN = 'isis2503-mario-hurtado.auth0.com'
SOCIAL_AUTH_AUTH0_KEY = '3RjFMK9vYNiyscvziRLrdzG9KnXx9wrt'
SOCIAL_AUTH_AUTH0_SECRET = 'gWfwJBhNuXyiRUcHtLWF4C1a_Ll7FudCYZb80HH-DKyiCKO4I54-FcmJxlPBt3P_'

SOCIAL_AUTH_AUTH0_SCOPE = [
   'openid', 'profile'
]

AUTHENTICATION_BACKENDS = {
   'monitoring.auth0backend.Auth0',
   'django.contrib.auth.backends.ModelBackend',
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

ROOT_URLCONF = 'monitoring.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR , 'monitoring', 'templates')],
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


WSGI_APPLICATION = 'monitoring.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    #'default': {
      # 'ENGINE': 'django.db.backends.postgresql_psycopg2',
     #   'NAME': 'canemdb',
    #    'USER': 'canem',
    #    'PASSWORD': 'canemchiper',
   #     'HOST': '172.24.42.128',
   #   'PORT': '5432',
   #}

        #'default': {
      #'ENGINE': 'django.db.backends.sqlite3',
       #  'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
     #}

     'default': {
     'ENGINE': 'django.db.backends.postgresql_psycopg2',
     'NAME': 'canemdb',
     'USER': 'canem',
     'PASSWORD': 'canemchiper',
     'HOST': 'canemdb.cxzelxrt5fdl.us-east-1.rds.amazonaws.com',
     'PORT': '5432',
    }

}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
