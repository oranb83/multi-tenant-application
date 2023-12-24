import logging

from django.conf import settings
from rest_framework.routers import DefaultRouter

from api.utils import get_current_request

logger = logging.getLogger()
logging.basicConfig(level=logging.DEBUG)


class TenantBasedRouter(DefaultRouter):
    def db_for_read(self, model, **hints):
        # Retrieve the request object
        if request := get_current_request():
            if tenant_id := request.resolver_match.kwargs.get('id'):
                # Distribute every 3 tenants to different database servers.
                # Every three consecutive tenant IDs are mapped to the same DB together.
                # Note: I did not implement a dynamic creation of the databases since it's
                #       out of scope.
                db_server_index = (int(tenant_id) - 1) // 3
                # Defensive programming: make sure we don't exceed the number of active DB servers
                # I decided in this implementation to continue with the servers distribution
                # sequence, but I can also raise an error.
                amount_of_active_db_servers = len(settings.DATABASES) - 1  # subtracting the default DB
                db_server_index %= amount_of_active_db_servers
                db_server_index += 1  # Adding 1 to skip db_server_0
                logging.debug(f'Using DB server #{db_server_index} for tenant #{tenant_id}')
                # Assuming database server names are db_server_1, db_server_2, db_server_3, etc.
                return f'db_server_{db_server_index}'

        # Return the default database if no tenant ID was found. I can also raise an error here.
        return 'default'

    def db_for_write(self, model, **hints):
        # Same logic as db_for_read since we want to use the same DB for read and write at the
        # moment
        return self.db_for_read(model, **hints)
