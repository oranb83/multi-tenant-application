from django.conf.urls import include, url

urlpatterns = [
    # The following URL pattern includes the 'multi_tenant_application.api.v1.urls' for a specific tenant.
    # The 'tenant_id' parameter in the URL is used to identify the specific tenant.
    # I can easily change it, with the urls.py files hirarchy, in case I need to create APIs
    # that will pass the tenant_id as a parameter in the URL.
    url(r'^v1/tenants/<int:tenant_id>/', include('multi_tenant_application.api.v1.urls'))
]
