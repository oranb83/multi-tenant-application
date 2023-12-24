from datetime import datetime

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from api.models.resources.models import Resource
from api.models.tenants.models import Tenant
from datetime import datetime
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.models.resources.models import Resource
from api.models.tenants.models import Tenant


class FindingListCreateViewTests(APITestCase):
    def setUp(self):
        self.tenant = Tenant.objects.create(id=1)  # Create a Tenant object
        self.resource = Resource.objects.create(unique_id='123', name='TestResource', cloud_account='AWS')  # Create a Resource object
        self.valid_test_data = {
            'external_id': '001',
            'type': 'Type A',
            'title': 'Title A',
            'severity': 'High',
            'created_at': datetime.now(),
            'sensor': 'Sensor A',
            'resource': self.resource,
            'id': self.tenant.id
        }


    class FindingListCreateViewTests(APITestCase):
        def setUp(self):
            self.tenant = Tenant.objects.create(id=1)  # Create a Tenant object
            self.resource = Resource.objects.create(unique_id='123', name='TestResource', cloud_account='AWS')  # Create a Resource object
            self.valid_test_data = {
                'external_id': '001',
                'type': 'Type A',
                'title': 'Title A',
                'severity': 'High',
                'created_at': datetime.now().isoformat(),
                'sensor': 'Sensor A',
                'resource': self.resource.unique_id,
                'tenant': self.tenant.id
            }

        def test_create_finding(self):
            url = reverse('finding-list-create', kwargs={'id': self.tenant.id})
            response = self.client.post(url, self.valid_test_data, format='json')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        def test_list_findings(self):
            url = reverse('finding-list-create', kwargs={'id': self.tenant.id})
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
