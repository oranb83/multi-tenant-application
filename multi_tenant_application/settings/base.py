# Base Settings File
import os

# Add your local settings here
SECRET_KEY = 'your_secret_key'
DEBUG = True  # Set to False in production

INSTALLED_APPS = [
    'multi-tenant_application.api',
    'multi-tenant_application.dynamic_db_router'
]

# Database router settings
DATABASE_ROUTERS = ['routers.TenantBasedRouter']

# Database configuration for PostgreSQL
DB_NAME = os.getenv('DB_NAME', 'multi_tenant_app')
DB_ENGINE = os.getenv('DB_ENGINE', 'django.db.backends.postgresql')
DB_PORT = os.getenv('DB_PORT', '5432')
DB_TEST_NAME = os.getenv('DB_TEST_NAME', 'multi_tenant_app')

DATABASES = {
    'default': {
        'ENGINE': DB_ENGINE,
        'NAME': DB_NAME,
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASSWORD'],
        'HOST': os.environ['DB_HOST'],
        'PORT': DB_PORT,
        'TEST': {'NAME': DB_TEST_NAME}
        # 'OPTIONS': {'charset': 'latin1'},
    }
}
