# Local Settings File
from .base import *

# Database configuration for PostgreSQL
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
    },
    'db_server_1': {
        # Configuration for database server 1
        'ENGINE': DB_ENGINE,
        'NAME': DB_NAME,
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASSWORD'],
        'HOST': os.environ['DB_HOST_1'],
        'PORT': DB_PORT,
        'TEST': {'NAME': DB_TEST_NAME}
    },
    'db_server_2': {
        # Configuration for database server 2
        'ENGINE': DB_ENGINE,
        'NAME': DB_NAME,
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASSWORD'],
        'HOST': os.environ['DB_HOST_2'],
        'PORT': DB_PORT,
        'TEST': {'NAME': DB_TEST_NAME}
    },
    'db_server_3': {
        # Configuration for database server 3
        'ENGINE': DB_ENGINE,
        'NAME': DB_NAME,
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASSWORD'],
        'HOST': os.environ['DB_HOST_3'],
        'PORT': DB_PORT,
        'TEST': {'NAME': DB_TEST_NAME}
    }
}
