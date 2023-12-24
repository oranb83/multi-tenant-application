from django.conf import settings
from dynamic_db_router.router import DynamicDbRouter


class TenantBasedRouter(DynamicDbRouter):
    def db_for_read(self, model, **hints):
        # Retrieve the request object
        request = hints.get('request')
        if request:
            # Extract 'tenant_id' from the URL parameters or URL path
            tenant_id = request.parser_context['kwargs'].get('id')

            # Map 'id' to a database.
            # Modify this logic based on your database mappings.
            # Distribute every 3 tenants to different database servers.
            if tenant_id:
                # Every three consecutive tenant IDs are mapped to the same DB together
                # Note: I did not implement a dynamic creation of the databases since it's
                #       out of scope
                db_server_index = (int(tenant_id) - 1) // 3
                # Defensive programming: make sure we don't exceed the number of active DB servers
                # I decided in this implementation to continue with the servers distribution
                # sequence, but I can also raise a configuration error
                amount_of_active_db_servers = len(settings.DATABASES) - 1  # subtracting the default DB
                db_server_index %= amount_of_active_db_servers + 1
                # Assuming database server names are db_server_1, db_server_2, db_server_3, etc.
                return f'db_server_{db_server_index}'

        # Return the default database if no tenant ID was found. I can also raise an error here,
        # but it will break my shell_plus command for RUD operations.
        return 'default'
