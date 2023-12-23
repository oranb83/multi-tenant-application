from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from mixer.backend.django import mixer
from ..models import Finding
from ..serializers import FindingSerializer

class TestFindingsAPI(APITestCase):
    def setUp(self):
        self.finding = mixer.blend(Finding)

    def test_list_findings(self):
        url = reverse('findings-list-create', kwargs={'tenant_id': 'sample_tenant_id'})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        # Add more assertions for response data if required

    def test_create_finding(self):
        url = reverse('findings-list-create', kwargs={'tenant_id': 'sample_tenant_id'})
        data = {
            'external_id': 'abc123',
            'type': 'Sample Type',
            'title': 'Sample Title',
            # Add other required fields here
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Add more assertions for successful creation if needed
