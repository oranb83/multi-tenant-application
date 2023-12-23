from django.conf.urls import url, include

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Note: this code will be moved to a common folder if we have more than one app.
schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="API Documentation for Multi-Tenant Application",
    ),
    public=True,
)

urlpatterns = [
    # Swagger Endpoint
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    # API Endpoints
    url(r'^findings/', include('api.v1.findings.urls')),
]
