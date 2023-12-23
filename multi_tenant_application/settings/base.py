# Base Settings File
import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

# Add your local settings here
SECRET_KEY = 'your_secret_key'
DEBUG = True  # Set to False in production


# Application definition
INSTALLED_APPS = [
    'django.contrib.contenttypes',  # Enable content types
    "api",  # Application definition
    "rest_framework",  # Enable rest framework
    'dynamic_db_router'  # Enable DB router
]

ROOT_URLCONF = "multi_tenant_application.urls"

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Database router settings
DATABASE_ROUTERS = ['routers.TenantBasedRouter']

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
