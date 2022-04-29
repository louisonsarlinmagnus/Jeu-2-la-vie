import os

ALLOWED_HOSTS = ['j2lv.lsarlinmagnus.fr']
DEBUG = False
DEFAULT_FROM_EMAIL = 'louisonsm.pro@gmail.com'

INSTALLED_APPS = [
    'jeuDeLaVie.apps.JeudelavieConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
    },
]