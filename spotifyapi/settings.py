import os
import dj_database_url
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'api',
    'rest_framework.authtoken',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.spotify',
    'corsheaders'
]

env = os.environ.get('ENV', None)

DEBUG = True
LOGIN_REDIRECT_URL = 'http://localhost:8000'
ACCOUNT_LOGOUT_REDIRECT_URL = 'http://localhost:8000'

SPOTIFY_WEB_URL =  os.environ.get('SPOTIFY_WEB_URL')
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'sdfdslfjsdfjsdlfjsdfjsdlfjsldfjsfsdfsdjhfskh'
CACHE_FILE = os.path.join(BASE_DIR, 'django_cache')
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': CACHE_FILE,
    }
}

SOCIALACCOUNT_PROVIDERS = {
    'spotify': {
        'SCOPE': [
            'user-read-currently-playing',
        ],
    }
}

SOCIALACCOUNT_QUERY_EMAIL = True
SITE_ID = 1
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_ADAPTER = 'api.account_adapter.MyAccountAdapter'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True
ALLOWED_HOSTS = ['*']
ROOT_URLCONF = 'spotifyapi.urls'
AUTHENTICATION_BACKENDS = (
    
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
    
)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates",)],
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

WSGI_APPLICATION = 'spotifyapi.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases



EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    )
}
REACT_APP_DIR = os.path.join(BASE_DIR, 'spotify')
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [		
     os.path.join(REACT_APP_DIR, 'build', 'static')		
]

if os.environ.get('ENV') == 'staging':
    MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware',]
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    ALLOWED_HOSTS = ['*']
    DEBUG = False
    LOGIN_REDIRECT_URL = '/'
    ACCOUNT_LOGOUT_REDIRECT_URL = '/'
    db_from_env = dj_database_url.config()
    DATABASES['default'].update(db_from_env)
