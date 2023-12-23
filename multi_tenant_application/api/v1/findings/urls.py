from django.conf.urls import url
from .views import FindingListCreateView


urlpatterns = [
    url(r'^$', FindingListCreateView.as_view(), name='findings-list-create')
]
