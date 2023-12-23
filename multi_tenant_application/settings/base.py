# Base Settings File

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
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',       # Replace with your PostgreSQL database name
        'USER': 'your_db_user',       # Replace with your PostgreSQL username
        'PASSWORD': 'your_password',  # Replace with your PostgreSQL password
        'HOST': 'localhost',          # Replace with your PostgreSQL host (e.g., 'localhost')
        'PORT': '',                   # Leave empty for default PostgreSQL port (5432)
    }
}
