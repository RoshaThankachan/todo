"""
Django settings for to_do_project project.
"""

import os
<<<<<<< HEAD
=======
import dj_database_url  # New: For Render Database connection
>>>>>>> 5f82e1f377a9e4e32cf6dfa7a4536a922a0ad92b
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

<<<<<<< HEAD
# SECURITY
SECRET_KEY = 'your-secret-key-here'

DEBUG = True  # Keep True for now

ALLOWED_HOSTS = ['yourusername.pythonanywhere.com']

# APPLICATIONS
=======
# --- SECURITY ---
# On Render, set this in Environment Variables. Locally, it uses the default.
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-k_gu06cjgec!p)s&8#%^mxu9a(ce%!2ut*6l1*!^5z5s6tw*l)')

# DEBUG should be True for dev, False for Render
DEBUG = os.environ.get('DEBUG', 'True').lower() == 'true'

# Allow Render's domain and local host
ALLOWED_HOSTS = ['*'] 
CSRF_TRUSTED_ORIGINS = ['https://*.onrender.com']

# --- APPLICATION DEFINITION ---
>>>>>>> 5f82e1f377a9e4e32cf6dfa7a4536a922a0ad92b
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles', # Required for CSS/JS
    'todoapp',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # NEW: Must be right after SecurityMiddleware
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'to_do_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'to_do_project.wsgi.application'

<<<<<<< HEAD
# DATABASE (SQLite)
=======
# --- DATABASE ---
# This looks for Render's DATABASE_URL. If missing (local), it falls back to SQLite.
>>>>>>> 5f82e1f377a9e4e32cf6dfa7a4536a922a0ad92b
DATABASES = {
    'default': dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
        conn_max_age=600
    )
}

<<<<<<< HEAD
# PASSWORD VALIDATION
=======
# --- AUTHENTICATION ---
>>>>>>> 5f82e1f377a9e4e32cf6dfa7a4536a922a0ad92b
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

<<<<<<< HEAD
# INTERNATIONALIZATION
=======
# --- INTERNATIONALIZATION ---
>>>>>>> 5f82e1f377a9e4e32cf6dfa7a4536a922a0ad92b
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

<<<<<<< HEAD
# STATIC FILES
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
=======
# --- STATIC FILES (WhiteNoise) ---
STATIC_URL = 'static/'

# Required for production: where Django puts files after 'collectstatic'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Enables compression and caching (makes your site faster)
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
>>>>>>> 5f82e1f377a9e4e32cf6dfa7a4536a922a0ad92b
