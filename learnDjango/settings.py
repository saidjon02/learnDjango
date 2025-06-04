from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_0o8=&&2jsk9t6(!v$=vn=jp+1=j4*n$uz!^k-yqgja5ymqsp%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'rest_framework',
    'myapp',
    'rest_framework_simplejwt',
    'corsheaders',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# CORS sozlamalari (frontend bilan ishlash uchun)
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",  # Frontend manzili (React yoki boshqa)
]
CORS_ALLOW_CREDENTIALS = True
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'learnDjango.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'learnDjango.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Login sozlamalari
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/profile/'

# Password validation
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

# Til va vaqt
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = 'static/'
# settings.py
# Auto Field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 💌 EMAIL SOZLAMALARI — sinov uchun console'ga chiqaradi
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Agar haqiqiy email jo‘natmoqchi bo‘lsang, quyidagilarni yoz:


# settings.py
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'fozilovsaidjon71@gmail.com'
EMAIL_HOST_PASSWORD = 'saidjon123!!!'
DEFAULT_FROM_EMAIL = 'fozilovsaidjon71@gmail.com'

# 🔐 XAVFSIZLIK SOZLAMALARI
SECURE_SSL_REDIRECT = False         # HTTPS talab qilinmaydi
CSRF_COOKIE_SECURE = False          # CSRF cookie HTTPSsiz ham ishlaydi
SESSION_COOKIE_SECURE = False       # Session cookie HTTPSsiz ishlaydi
CSRF_COOKIE_HTTPONLY = True         # CSRF cookie JavaScript orqali ko‘rinmaydi
SECURE_BROWSER_XSS_FILTER = True    # XSS hujumlariga qarshi filtr


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}