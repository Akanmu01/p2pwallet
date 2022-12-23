import os
from pathlib import Path
from datetime import timedelta
import dj_database_url


DEBUG = os.getenv('DEBUG')



BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = os.path.join(BASE_DIR,'templates')
STATIC_DIR=os.path.join(BASE_DIR,'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
# COMPRESS_ROOT = os.path.join(BASE_DIR,'static')
# COMPRESS_ENABLED = True
# STATICFILES_FINDERS = ('compressor.finders.CompressorFinder',)

FLW_PUB_KEY =  os.getenv('FLW_PUB_KEY')#"FLWPUBK_TEST-a0666fd92afc005feb8725a5364e3157-X"
FLW_SEC_KEY =  os.getenv('FLW_SEC_KEY')#"FLWSECK_TEST-afbb6778d2b9fc007b0ab9aa76d2b3e3-X"
SECRET_KEY = os.getenv('SECRETKEY')
#'w+$mxf#dx87f$*3nut6vnma*9uk6x#d_qo8@wffv^+@l$w=v'


DEBUG = True
# DEBUG = os.getenv('DEBUG')

    
ALLOWED_HOSTS = ['*']

PREPEND_WWW = False
SERVER_EMAIL = 'root@localhost'
DEFAULT_FROM_EMAIL = 'webmaster@localhost'


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'rest_framework',
    'rest_framework_swagger',
    'drf_yasg',
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

REST_FRAMEWORK = {
        'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema'
    }


ROOT_URLCONF = 'p2pwallet.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['template'],
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

WSGI_APPLICATION = 'p2pwallet.wsgi.application'


DATABASES = {
    'default': dj_database_url.config(
        default='os.getenv('P2PWALLET_DATABASE')',
        conn_max_age=600
    )
}

# postgres://p2pwallet:YMD114tFWkAPWW07IGtBW0BNKYCtemV6@dpg-ceiq0t4gqg4dlfcmnqgg-a.oregon-postgres.render.com/p2pwallet



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



LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Africa/Lagos'

USE_I18N = True

USE_L10N = True

USE_TZ = True




AUTH_USER_MODEL = 'core.User'


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES':[
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES' :[
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ],
    'DEFAULT_PAGINATION_CLASS': 
        'rest_framework.pagination.LimitOffsetPagination',
        'PAGE_SIZE': 10,
    # 'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

JWT_AUTH = { 
    'JWT_VERIFY': True,
    'JWT_VERIFY_EXPIRATION': True,
    'JWT_EXPIRATION_DELTA': timedelta(days=1),
    'JWT_AUTH_HEADER_PREFIX': 'Bearer',
}


ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = '/?verification=1'
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = '/?verification=1'

SITE_ID = 1
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
