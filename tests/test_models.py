import pytest
from django.utils import timezone

from api.models.findings.models import Finding
from api.models.resources.models import Resource
from api.models.tenants.models import Tenant


@pytest.mark.django_db
def test_finding_model():
    # Create a sample resource and tenant
    resource = Resource.objects.create(name='Sample Resource')
    tenant = Tenant.objects.create(name='Sample Tenant')

    # Create a sample Finding
    finding = Finding.objects.create(
        external_id='123',
        type='Type',
        title='Title',
        severity=Finding.SeverityChoices.HIGH,
        created_at=timezone.now(),
        sensor='Sensor',
        resource=resource,
        tenant_id=tenant
    )

    # Assert the values of the created Finding
    assert finding.external_id == '123'
    assert finding.type == 'Type'
    assert finding.title == 'Title'
    assert finding.severity == Finding.SeverityChoices.HIGH
    assert finding.created_at is not None
    assert finding.sensor == 'Sensor'
    assert finding.resource == resource
    assert finding.tenant == tenant

    # Test the __str__ method
    assert str(finding) == '123'

    # Test the unique_together constraint
    with pytest.raises(Exception):
        Finding.objects.create(
            external_id='123',
            type='Type',
            title='Title',
            severity=Finding.SeverityChoices.HIGH,
            created_at=timezone.now(),
            sensor='Sensor',
            resource=resource,
            tenant_id=tenant
        )
