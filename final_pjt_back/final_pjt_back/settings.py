from pathlib import Path

import os
import environ


# django-environ 설정
env = environ.Env(
    DEBUG=(bool, False),
)

BASE_DIR = Path(__file__).resolve().parent.parent

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
DEBUG = env('DEBUG')

FINLIFE_API_KEY = env('FINLIFE_API_KEY')
FINANCE_API_URL = env('FINANCE_API_URL')
OPENAI_API_KEY = env('OPENAI_API_KEY')

# ==========================================================
# CORE SETTINGS
# ==========================================================
SECRET_KEY = 'django-insecure-owop#w6fhr)lu1un_j)jsfp1n24b$rcwhacf7)h8-m1z+3-j=%'
DEBUG = True
ALLOWED_HOSTS = []
ROOT_URLCONF = 'final_pjt_back.urls'
WSGI_APPLICATION = 'final_pjt_back.wsgi.application'

# ==========================================================
# APPS SETTINGS
# ==========================================================
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
]

PROJECT_APPS = [
    'accounts',
    'articles',
    'finances',
]

THIRD_PARTY_APPS = [
    # API & CORS
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    
    # Authentication
    'allauth',
    'allauth.account', 
    'allauth.socialaccount',
    'dj_rest_auth',
    'dj_rest_auth.registration',
]

INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS + THIRD_PARTY_APPS

# ==========================================================
# MIDDLEWARE SETTINGS
# ==========================================================
MIDDLEWARE = [
    # Security
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    # Sessions & Authentication
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    
    # Common
    'django.middleware.common.CommonMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    
    # CORS
    'corsheaders.middleware.CorsMiddleware',
]

# ==========================================================
# AUTHENTICATION SETTINGS
# ==========================================================
AUTH_USER_MODEL = 'accounts.User'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
}

# custom register serializer
REST_AUTH = {
    'REGISTER_SERIALIZER': 'accounts.serializers.CustomRegisterSerializer',
}


AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ==========================================================
# CORS SETTINGS
# ==========================================================
CORS_ALLOWED_ORIGINS = [
    'http://127.0.0.1:5173',
    'http://localhost:5173',
]

# ==========================================================
# TEMPLATES SETTINGS
# ==========================================================
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

# ==========================================================
# DATABASE SETTINGS
# ==========================================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ==========================================================
# INTERNATIONALIZATION SETTINGS
# ==========================================================
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ==========================================================
# STATIC & MEDIA FILES SETTINGS
# ==========================================================
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ==========================================================
# OTHER SETTINGS
# ==========================================================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'