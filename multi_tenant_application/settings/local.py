# Local Settings File
from .base import *

# Database configuration for PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',       # Replace with your PostgreSQL database name
        'USER': 'your_db_user',       # Replace with your PostgreSQL username
        'PASSWORD': 'your_password',  # Replace with your PostgreSQL password
        'HOST': 'localhost',          # Replace with your PostgreSQL host (e.g., 'localhost')
        'PORT': '',                   # Leave empty for default PostgreSQL port (5432)
    },
    'db_server_1': {
        # Configuration for database server 1
        # ...
    },
    'db_server_2': {
        # Configuration for database server 2
        # ...
    },
    'db_server_3': {
        # Configuration for database server 3
        # ...
    }
}
