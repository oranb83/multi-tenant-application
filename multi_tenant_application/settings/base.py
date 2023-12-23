# Base Settings File
import os

# Add your local settings here
SECRET_KEY = 'your_secret_key'
DEBUG = True  # Set to False in production

INSTALLED_APPS = [
    'api',
    'dynamic_db_router'
]

# Database router settings
DATABASE_ROUTERS = ['routers.TenantBasedRouter']

# Database configuration for PostgreSQL
DB_NAME = os.getenv('DB_NAME', 'new_portal_v2')
DB_ENGINE = os.getenv('DB_ENGINE', 'psqlextra.backend')
DB_PORT = os.getenv('DB_PORT', '5432')
DB_TEST_NAME = os.getenv('DB_TEST_NAME', 'portal_v2_test')

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
