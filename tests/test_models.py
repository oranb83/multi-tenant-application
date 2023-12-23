import pytest
from mixer.backend.django import mixer

from api.v1.findings.models import Finding


pytestmark = pytest.mark.django_db

def test_finding_model():
    # Create a sample Finding object using Mixer
    finding = mixer.blend(Finding)

    # Perform assertions to test model behavior
    assert finding.pk is not None
    assert isinstance(finding, Finding)
    assert str(finding) == f"Finding {finding.pk}: {finding.title}"
    # Add more assertions as needed
