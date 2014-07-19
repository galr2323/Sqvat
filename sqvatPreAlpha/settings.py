"""
Django settings for sqvatPreAlpha project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
SETTINGS_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_PATH = os.path.abspath(os.path.dirname(__name__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'tc&t!q70ggm7lrl_#-49krbtothwdvm%)m(@2)d@#2)zogp=e9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mainApp',
    'django.contrib.admin',
    'south',
    'crispy_forms',
    'debug_toolbar',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'sqvatPreAlpha.urls'

WSGI_APPLICATION = 'sqvatPreAlpha.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_PATH, 'sqvat.db'),
    }
}

DATABASE_PATH = os.path.join(PROJECT_PATH, 'sqvat.db')



# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True





# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = ('C:/Users/GAL/PycharmProjects/sqvatPreAlpha/static/',)

#templates
TEMPLATE_PATH = os.path.join(PROJECT_PATH, 'templates')


TEMPLATE_DIRS = ('C:/Users/GAL/PycharmProjects/sqvatPreAlpha/templates/',)

#media

MEDIA_ROOT =  'C:/Users/GAL/PycharmProjects/sqvatPreAlpha/media/'

MEDIA_URL = '/media/'

#login
LOGIN_URL = '/sign_in/'

CRISPY_TEMPLATE_PACK = 'bootstrap3'