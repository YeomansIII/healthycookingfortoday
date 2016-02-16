"""
Django settings for settings project.

Generated by 'django-admin startproject' using Django 1.8.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_PATH = (os.path.join(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))), '..'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

DEBUG = True
ALLOWED_HOSTS = ['']

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

REDACTOR_OPTIONS = {'lang': 'en'}
REDACTOR_UPLOAD = 'uploads/'

FROALA_UPLOAD_PATH = 'uploads/images'
FROALA_EDITOR_PLUGINS = ('align', 'char_counter', 'code_beautifier', 'code_view', 'colors', 'emoticons',
                         'entities', 'file', 'font_family', 'font_size', 'fullscreen', 'image', 'image_manager', 'inline_style',
                         'line_breaker', 'link', 'lists', 'paragraph_format', 'paragraph_style', 'quote', 'save', 'table',
                         'url', 'video')
# Application definition

INSTALLED_APPS = (
    'jet',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'settings',
    'taggit',
    'frontend',
    'blogger',
    'django_summernote',
    'blanc_basic_assets'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'settings.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

BLOG_SETTINGS = {
    'defaults': {  # change the defaults of models and some constats for views
        'auto_publish': False,
        'auto_promote': False,
    },
    'info': {  # attached to all responses so the information is available to the templates.
        'BLOG_TITLE': 'Healthy Cooking for Today',
        'BLOG_SUBTITLE': 'By Marianne Yeomans',
    }
}

SUMMERNOTE_CONFIG = {
    # Using SummernoteWidget - iframe mode
    'iframe': False,  # or set False to use SummernoteInplaceWidget - no iframe mode

    # Using Summernote Air-mode
    'airMode': False,

    # Use native HTML tags (`<b>`, `<i>`, ...) instead of style attributes
    # (Firefox, Chrome only)
    'styleWithTags': True,

    # Set text direction : 'left to right' is default.
    'direction': 'ltr',

    # Change editor size
    'width': '600px',
    'height': '400px',

    # Use proper language setting automatically (default)
    'lang': None,

    # Customize toolbar buttons
    'toolbar': [
        ['style', ['style']],
        ['style', ['bold', 'italic', 'underline', 'clear']],
        ['para', ['ul', 'ol', 'paragraph']],
        ['insert', ['link', 'picture', 'video', 'table', 'hr']],
    ],

    # Need authentication while uploading attachments.
    'attachment_require_authentication': True,
}

WSGI_APPLICATION = 'settings.wsgi.application'

import ldap
from django_auth_ldap.config import LDAPSearch, PosixGroupType

AUTH_LDAP_SERVER_URI = "ldap://yeomans.io"

AUTH_LDAP_GROUP_SEARCH = LDAPSearch("ou=groups,dc=yeomans,dc=io",
                                    ldap.SCOPE_SUBTREE,
                                    "(objectClass=posixGroup)"
                                    )
AUTH_LDAP_GROUP_TYPE = PosixGroupType()
AUTH_LDAP_CACHE_GROUPS = True

AUTH_LDAP_REQUIRE_GROUP = "cn=healthycookingdjango,ou=groups,dc=yeomans,dc=io"
AUTH_LDAP_USER_ATTR_MAP = {"first_name": "givenName", "last_name": "sn"}
AUTH_LDAP_USER_FLAGS_BY_GROUP = {
    "is_staff": "cn=healthycookingdjangodev,ou=groups,dc=yeomans,dc=io",
    "is_superuser": "cn=healthycookingdjangodevsuper,ou=groups,dc=yeomans,dc=io"
}

AUTH_LDAP_BIND_DN = ""
AUTH_LDAP_BIND_PASSWORD = ""
AUTH_LDAP_USER_SEARCH = LDAPSearch("ou=users,dc=yeomans,dc=io",
                                   ldap.SCOPE_SUBTREE, "(uid=%(user)s)")

AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
)


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'development!key!**only**'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'healthycookingdb',
    },
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'build/static'),
    os.path.join(BASE_DIR, 'froala_editor/static'),
)
