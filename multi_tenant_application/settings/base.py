# Base Settings File
import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

# Add your local settings here
SECRET_KEY = 'your_secret_key'
DEBUG = True  # Set to False in production


# Application definition
INSTALLED_APPS = [
    'api',  # Application definition
    'drf_yasg',
    # 'django-filter',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    'rest_framework',  # Enable rest framework
    'dynamic_db_router',  # Enable DB router
    'django_extensions'
]

ROOT_URLCONF = 'multi_tenant_application.urls'

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "multi_tenant_application.wsgi.application"

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MIDDLEWARE = [
    # Django's built-in middleware classes
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
]

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "static"
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages"
            ]
        },
    }
]

REST_FRAMEWORK = {
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.NamespaceVersioning',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # Note: use JWTAutentication for a real application instead of the TokenAuthentication
        'rest_framework.authentication.TokenAuthentication',  # Example: Token Authentication
        'rest_framework.authentication.SessionAuthentication',  # Example: Session Authentication
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',  # Allow any access, no authentication required
        # Note: wwitch to this one for production:
        # 'rest_framework.permissions.IsAuthenticated',  # Only authenticated users have permissions
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer'
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',

    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100,  # Example: Default page size for pagination
    # 'DEFAULT_FILTER_BACKENDS': (
    #     'django_filters.rest_framework.DjangoFilterBackend',
    #     'rest_framework.filters.SearchFilter'
    # ),
    'TEST_REQUEST_RENDERER_CLASSES': (
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
        "rest_framework_csv.renderers.CSVStreamingRenderer",
        "api.renderers.FlatCSVStreamingRenderer",
    ),
    "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.coreapi.AutoSchema",
    # Note: implement to catch all exceptions since we don't want to expose any unhandled errors
    # "EXCEPTION_HANDLER": "api.global_exceptions_handler.custom_exception_handler",
}

# Database router settings
DATABASE_ROUTERS = ['multi_tenant_application.routers.TenantBasedRouter']

# Database configuration for PostgreSQL
DB_ENGINE = os.getenv('DB_ENGINE', 'django.db.backends.postgresql')
DB_NAME = os.getenv('DB_NAME', 'multi_tenant_app')
DB_USER = os.getenv('DB_USER', 'root')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'root')
DB_HOST = os.getenv('DB_HOST', '127.0.0.1')
DB_PORT = os.getenv('DB_PORT', '5432')
DB_TEST_NAME = os.getenv('DB_TEST_NAME', 'test_multi_tenant_app')

DATABASES = {
    'default': { # I must define a default since it's how Django works
        'ENGINE': DB_ENGINE,
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'HOST': DB_HOST,
        'PORT': DB_PORT,
        'TEST': {'NAME': DB_TEST_NAME}
        # 'OPTIONS': {'charset': 'latin1'},
    }
}
