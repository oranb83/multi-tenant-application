from dynamic_db_router.router import DynamicDbRouter


class TenantBasedRouter(DynamicDbRouter):
    def db_for_read(self, model, **hints):
        # Retrieve the request object
        request = hints.get('request')

        if request:
            # Extract 'tenant_id' from the URL parameters or URL path
            tenant_id = request.parser_context['kwargs'].get('tenant_id')

            # Map 'tenant_id' to a database.
            # Modify this logic based on your database mappings.
            # Distribute every 3 tenants to different database servers.
            if tenant_id:
                # Distribute based on the last digit of tenant ID.
                # Note: I did not implement a dynamic creation of the databases since it's out of scope
                server_index = (int(tenant_id) % 3)
                # Assuming database server names are db_server_1, db_server_2, db_server_3.
                return f'db_server_{server_index + 1}'

        # Default to 'default' database if tenant ID is not provided.
        return 'default'
