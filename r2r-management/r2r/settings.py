"""
Django settings for r2r project.

Generated by 'django-admin startproject' using Django 5.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os

from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables
load_dotenv(os.path.join(BASE_DIR, ".env"))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG", "False") == "True"

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split(",")

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Dependenecy App
    "storages",
    # Internal App
    "apps",
    "expenses",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "r2r.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.i18n",
            ],
        },
    },
]

WSGI_APPLICATION = "r2r.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_DB"),
        "USER": os.getenv("POSTGRES_USER"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"
LANGUAGE_CODE = "zh-hans"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Define supported languages
LANGUAGES = [
    ("en", "English"),
    ("zh-hans", "简体中文"),
]

# Locale paths for translation files
LOCALE_PATHS = [
    os.path.join(BASE_DIR, "locale"),
]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"

# Add this near your static files configuration
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# Then your Azure storage configuration
# Static files (CSS, JavaScript, Images)
USE_AZURE: bool = (
    os.getenv("USE_AZURE") == "True"
)  # Make sure it's properly converted to boolean

if USE_AZURE:
    # Azure Storage Settings
    AZURE_ACCOUNT_NAME = os.getenv("AZURE_ACCOUNT_NAME")
    AZURE_CUSTOM_DOMAIN = f"{AZURE_ACCOUNT_NAME}.blob.core.windows.net"

    # Static and Media Files Configuration
    STATIC_URL = f'https://{AZURE_CUSTOM_DOMAIN}/{os.getenv("STATIC_LOCATION")}/'
    MEDIA_URL = f'https://{AZURE_CUSTOM_DOMAIN}/{os.getenv("MEDIA_LOCATION")}/'

    # Storage Configuration
    STORAGES = {
        "default": {  # For media files
            "BACKEND": "storages.backends.azure_storage.AzureStorage",
            "OPTIONS": {
                "connection_string": os.getenv("AZURE_CONNECTION_STRING"),
                "azure_container": os.getenv("MEDIA_LOCATION"),
            },
        },
        "staticfiles": {  # For static files
            "BACKEND": "storages.backends.azure_storage.AzureStorage",
            "OPTIONS": {
                "connection_string": os.getenv("AZURE_CONNECTION_STRING"),
                "azure_container": os.getenv("STATIC_LOCATION"),
            },
        },
    }

    # Only include STATICFILES_DIRS if the directory exists
    static_dir = os.path.join(BASE_DIR, "static")
    if os.path.exists(static_dir):
        STATICFILES_DIRS = [static_dir]

else:
    # Local development settings
    STATIC_URL = "static/"
    MEDIA_URL = "/media/"
    MEDIA_ROOT = os.path.join(BASE_DIR, "media")
    STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
