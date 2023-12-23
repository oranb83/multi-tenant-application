from django.conf.urls import url
from .views import FindingListCreateView


urlpatterns = [
    url(r'tenants/<int:tenant_id>/findings/', FindingListCreateView.as_view(),
         name='findings-list-create')
]
