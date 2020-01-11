"""
Django settings for helm project.

Generated by 'django-admin startproject' using Django 2.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_#tjbm#5rrj)@b0l48&=tpkidqlg9o^sww16=a8v73buiw8*xf'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites', # new

    'allauth', # new
    'allauth.account', # new
    'allauth.socialaccount', # new
    'allauth.socialaccount.providers.google', # new

    'bootstrap4', # new
    'static_precompiler', #new
    'debug_toolbar', #new

    'app', # new
    'users', # new
    'pages',  # new
    'resume',  # new
    'engineering',  # new



]

# custom user model
AUTH_USER_MODEL = 'users.CusetomUser' # new

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'helm.urls'

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
                'app.processor.debug_context'
            ],
        },
    },
]
WSGI_APPLICATION = 'helm.wsgi.application'

# all auth
AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

if 'RDS_HOSTNAME' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
        }
    }
else:
    DATABASES = {
        'default': {
            'NAME': 'helm_v3',
            'ENGINE': 'django.db.backends.mysql',
            'USER': 'root',
            'PASSWORD': 'mysql',
            'OPTIONS': {
                'autocommit': True,
            },
        }
    }

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'helm_static')
]


# for default
LOGIN_REDIRECT_URL = 'deshboard'
LOGOUT_REDIRECT_URL = 'home'


# all auth
SITE_ID = 1

ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_SIGNUP_PASSWORD_VERIFICATION = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_FORMS = {'signup': 'users.forms.MyCustomSignupForm'}


# default with django for emil
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_USE_TLS = True
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_PASSWORD = '9970fbdk'  # my gmail password
# EMAIL_HOST_USER = 'dishakotadiya00@gmail.com'  # my gmail username
# EMAIL_PORT = 587
# DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


# sendgrid email
SENDGRID_API_KEY = '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'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = SENDGRID_API_KEY
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'jigneshkotadiya000@gmail.com'


# Contact page details
CONTACT_EMAIL = 'jigneshkotadiya000@gmail.com'

# for pre compiler
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders..
    # 'static_precompiler.finders.StaticPrecompilerFinder',
)

STATIC_PRECOMPILER_OUTPUT_DIR = os.path.join(BASE_DIR, 'helm_static/compiled')
STATIC_PRECOMPILER_DISABLE_AUTO_COMPILE = False
STATIC_PRECOMPILER_COMPILERS = (
    ('static_precompiler.compilers.libsass.SCSS', {
        "sourcemap_enabled": True,
        # "load_paths": ["/path"],
        "precision": 8,
        # "output_style": "compressed",
    }),
    ('static_precompiler.compilers.libsass.SASS', {
        "sourcemap_enabled": True,
        "load_paths": ["/path"],
        "precision": 8,
        "output_style": "compressed",
    }),
)


# djano debug
INTERNAL_IPS = [
    # ...
    '127.0.0.1',
    # ...
]