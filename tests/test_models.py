import pytest
from django.utils import timezone
from api.models.findings.models import Finding
from api.models.resources.models import Resource
from api.models.tenants.models import Tenant


@pytest.mark.django_db
class TestFindingModel:
    def test_create_finding(self):
        resource = Resource.objects.create(
            unique_id='foo:bar:hello:world',
            name='s3 bucket',
            cloud_account='12314ff2a3'
        )
        tenant = Tenant.objects.create(id=1)

        finding = Finding.objects.create(
            external_id='123',
            type='Type',
            title='Title',
            severity=Finding.SeverityChoices.HIGH,
            created_at=timezone.now(),
            sensor='Sensor',
            resource=resource,
            tenant=tenant
        )
        assert finding.external_id == '123'
        assert finding.type == 'Type'
        assert finding.title == 'Title'
        assert finding.severity == Finding.SeverityChoices.HIGH
        assert finding.created_at is not None
        assert finding.sensor == 'Sensor'
        assert finding.resource == resource
        assert finding.tenant == tenant

    def test_finding_str(self):
        resource = Resource.objects.create(
            unique_id='foo:bar:hello:world',
            name='s3 bucket',
            cloud_account='12314ff2a3'
        )
        tenant = Tenant.objects.create(id=1)

        finding = Finding.objects.create(
            external_id='123',
            type='Type',
            title='Title',
            severity=Finding.SeverityChoices.HIGH,
            created_at=timezone.now(),
            sensor='Sensor',
            resource=resource,
            tenant=tenant
        )
        assert str(finding) == 'Title (123)'

    def test_different_severity(self):
        resource = Resource.objects.create(
            unique_id='foo:bar:hello:world',
            name='s3 bucket',
            cloud_account='12314ff2a3'
        )
        tenant = Tenant.objects.create(id=1)

        finding_low_severity = Finding.objects.create(
            external_id='456',
            type='Type',
            title='Title',
            severity=Finding.SeverityChoices.LOW,
            created_at=timezone.now(),
            sensor='Sensor',
            resource=resource,
            tenant=tenant
        )
        assert finding_low_severity.severity == Finding.SeverityChoices.LOW

    def test_empty_title(self):
        resource = Resource.objects.create(
            unique_id='foo:bar:hello:world',
            name='s3 bucket',
            cloud_account='12314ff2a3'
        )
        tenant = Tenant.objects.create(id=1)

        finding_empty_title = Finding.objects.create(
            external_id='789',
            type='Type',
            title='',
            severity=Finding.SeverityChoices.MEDIUM,
            created_at=timezone.now(),
            sensor='Sensor',
            resource=resource,
            tenant=tenant
        )
        assert finding_empty_title.title == ''
