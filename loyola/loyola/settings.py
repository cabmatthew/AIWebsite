"""
Django settings for loyola project.

Generated by 'django-admin startproject' using Django 5.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-6#rwil77)n-)=a$yvi1%=08g&_wr6r&34ma2bke&j*t0#w)bz6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'website',
    'users',
    'ckeditor',
    'ckeditor_uploader',
    'django.forms'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'loyola.urls'

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

WSGI_APPLICATION = 'loyola.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Static files (CSS, JavaScript, images)
STATIC_URL = '/static/'


# Directory where Django will collect static files during production
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


# Additional directories where Django will look for static files during development
STATICFILES_DIRS = [
      # Example additional directory
    os.path.join(BASE_DIR, 'static', 'assets', 'vendor',),
    os.path.join(BASE_DIR, 'static', 'assets', 'vendor', 'animate.css'),
    os.path.join(BASE_DIR, 'static', 'assets', 'vendor', 'aos'),
    os.path.join(BASE_DIR, 'static', 'assets', 'vendor', 'bootstrap', 'css'),
    os.path.join(BASE_DIR, 'static', 'assets', 'vendor', 'bootstrap', 'js'),
    os.path.join(BASE_DIR, 'static', 'assets', 'vendor', 'boxicons', 'css'),
    os.path.join(BASE_DIR, 'static', 'assets', 'vendor', 'boxicons', 'fonts'),
    os.path.join(BASE_DIR, 'static', 'assets', 'vendor', 'counterup'),
    os.path.join(BASE_DIR, 'static', 'assets', 'vendor', 'icofont'),
    os.path.join(BASE_DIR, 'static', 'assets', 'vendor', 'icofont', 'fonts'),
    os.path.join(BASE_DIR, 'static', 'assets', 'vendor', 'isotope-layout'),
    os.path.join(BASE_DIR, 'static', 'assets', 'vendor', 'jquery'),
    os.path.join(BASE_DIR, 'static', 'assets', 'vendor', 'jquery-sticky'),
    os.path.join(BASE_DIR, 'static', 'assets', 'vendor', 'jquery.easing'),
    os.path.join(BASE_DIR, 'static', 'assets', 'vendor', 'php-email-form'),
    os.path.join(BASE_DIR, 'static', 'assets', 'vendor', 'venobox'),
    os.path.join(BASE_DIR, 'static', 'assets', 'vendor', 'waypoints'),
    os.path.join(BASE_DIR, 'static', 'assets', 'img', 'instructor'),
]



# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CKEditor Settings
CKEDITOR_UPLOAD_PATH = 'ckeditor_upload_path/'
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js' 
CKEDITOR_CONFIGS = {
    'default':
        {
            'toolbar': 'full',
            'width': 'auto',
            'extraPlugins': ','.join([
                'codesnippet',
            ]),
        },
}

FORM_RENDERER = 'django.forms.renderers.TemplatesSetting'

LOGIN_URL='http://127.0.0.1:8000/users/nologin'
