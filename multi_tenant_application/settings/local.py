# Local Settings File
from .base import *


# Database configuration for PostgreSQL
DATABASES.update(
    {
        # I can also change the DB_USER and DB_PASSWORD to be different for each database server,
        # but I will keep it simple for now
        'db_server_1': {
            # Configuration for database server 1
            'ENGINE': DB_ENGINE,
            'NAME': DB_NAME,
            'USER': DB_USER,
            'PASSWORD': DB_PASSWORD,
            'HOST': DB_HOST,
            'PORT': DB_PORT,
            'TEST': {'NAME': DB_TEST_NAME}
        }
        # Note: relevant for the future, if we will need more than one database server, but it
        #       will be done in a new file called 'production.py' or 'staging.py', etc.
        #       I will also need to add the relevant environment variables to the Dockerfile.
        # 'db_server_2': {
        #     # Configuration for database server 2
        #            'ENGINE': DB_ENGINE,
        #            'NAME': DB_NAME,
        #            'USER': DB_USER,
        #            'PASSWORD': DB_PASSWORD,
        #            'HOST': os.environ['DB_HOST_2'],
        #            'PORT': DB_PORT,
        #            'TEST': {'NAME': DB_TEST_NAME}
        # },
        # 'db_server_3': {
        #     # Configuration for database server 3
        #            'ENGINE': DB_ENGINE,
        #            'NAME': DB_NAME,
        #            'USER': DB_USER,
        #            'PASSWORD': DB_PASSWORD,
        #            'HOST': os.environ['DB_HOST_3'],
        #            'PORT': DB_PORT,
        #            'TEST': {'NAME': DB_TEST_NAME}
        # },

        # Add more entries for additional databases if needed
    }
)
