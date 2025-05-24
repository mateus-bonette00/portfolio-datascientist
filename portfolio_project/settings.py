import os
from pathlib import Path
import dj_database_url

# ------------------------------------------------------------------------------
# BASE_DIR
# ------------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# ------------------------------------------------------------------------------
# SECRET_KEY & DEBUG
# ------------------------------------------------------------------------------
SECRET_KEY = os.environ.get(
    'SECRET_KEY',
    'django-insecure-fallback-inseguro-por-padrao'
)

DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# ------------------------------------------------------------------------------
# ALLOWED_HOSTS
# ------------------------------------------------------------------------------
# O Render injeta RENDER_EXTERNAL_HOSTNAME com algo como "seu-app.onrender.com"
# Se quiser fixar, substitua pelo seu domínio
RENDER_HOST = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_HOST:
    ALLOWED_HOSTS = ['localhost', '127.0.0.1', RENDER_HOST]
else:
    ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'portfolio-mateus-bonette.onrender.com']

# ------------------------------------------------------------------------------
# INSTALLED_APPS
# ------------------------------------------------------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'portfolio',        # sua app
]

# ------------------------------------------------------------------------------
# MIDDLEWARE
# ------------------------------------------------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # serve arquivos estáticos
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ------------------------------------------------------------------------------
# URLS & TEMPLATES
# ------------------------------------------------------------------------------
ROOT_URLCONF = 'portfolio_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # sua pasta de templates
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

WSGI_APPLICATION = 'portfolio_project.wsgi.application'

# ------------------------------------------------------------------------------
# DATABASES
# ------------------------------------------------------------------------------
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.config(
            conn_max_age=600,
            ssl_require=True
        )
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# ------------------------------------------------------------------------------
# PASSWORD VALIDATORS
# ------------------------------------------------------------------------------
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

# ------------------------------------------------------------------------------
# INTERNATIONALIZATION
# ------------------------------------------------------------------------------
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# ------------------------------------------------------------------------------
# STATIC FILES (CSS, JS, Images)
# ------------------------------------------------------------------------------
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
STATICFILES_STORAGE = (
    'whitenoise.storage.CompressedManifestStaticFilesStorage'
)

# ------------------------------------------------------------------------------
# MEDIA FILES (Uploads)
# ------------------------------------------------------------------------------
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ------------------------------------------------------------------------------
# EMAIL CONFIGURATION (formulário de contato)
# ------------------------------------------------------------------------------
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get('EMAIL_HOST', 'smtp.gmail.com')
EMAIL_PORT = int(os.environ.get('EMAIL_PORT', 587))
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', 'True') == 'True'
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# ------------------------------------------------------------------------------
# DEFAULT AUTO FIELD
# ------------------------------------------------------------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
