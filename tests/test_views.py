import pytest
from django.urls import reverse
from rest_framework import status

from api.models.findings.models import Finding
from api.models.resources.models import Resource
from api.models.tenants.models import Tenant


@pytest.mark.django_db(databases=['default', 'db_server_1'])
class TestFindingsAPI:
    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.tenant = Tenant(id=1)
        self.tenant.save()

        self.resource = Resource(
            unique_id='foo:bar:hello:world1',
            name='s3 bucket',
            cloud_account='12314ff2a3',
            tenant = self.tenant
        )
        self.resource.save()

        self.finding = Finding.objects.create(
            **{
                'external_id': 'myid1',
                'type': 'mytype',
                'title': 'my name is Oran',
                'severity': 'Critical',
                'created_at': '2023-12-24T15:32:15.032Z',
                'sensor': 'Orca',
                'resource': self.resource,
            }
        )

    def test_list_findings(self, client):
        # Arrange
        url = reverse('findings-list-create', kwargs={'id': self.tenant.id})

        # Act
        response = client.get(url)

        # Assert
        assert response.status_code == status.HTTP_200_OK


    def test_create_finding(self, client):
        # Arrange
        url = reverse('findings-list-create', kwargs={'id': self.tenant.id})
        data = {
            'external_id': 'myid2',
            'type': 'mytype',
            'title': 'my name is Oran',
            'severity': 'Critical',
            'created_at': '2023-12-24T15:32:15.032Z',
            'sensor': 'Orca',
            'resource': {
                'unique_id': 'foo:bar:hello:world',
                'name': 's3 bucket',
                'cloud_account': '12314ff2a3'
            }
        }

        # Act
        response = client.post(url, data, content_type='application/json')

        # Assert
        assert response.status_code == status.HTTP_201_CREATED
