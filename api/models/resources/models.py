from django.db import models

from api.models.tenants.models import Tenant


class Resource(models.Model):
    """
    Represents a resource in the multi-tenant application.

    @ivar unique_id: The unique identifier of the resource.
    @type unique_id: str

    @ivar name: The name of the resource.
    @type name: str

    @ivar cloud_account: The cloud account associated with the resource.
    @type cloud_account: str

    @ivar tenant: The tenant associated with the finding.
    @type tenant: Tenant

    @method __str__: Returns a string representation of the resource.

    @ivar Meta: Metadata for the resource.
    @type Meta: dict
    @ivar Meta.unique_together: Specifies the unique constraint for the resource.
    @type Meta.unique_together: tuple
    """
    unique_id = models.CharField(max_length=255, null=False, blank=False)
    name = models.CharField(max_length=255, null=False, blank=False)
    # AWS account IDs are 12-digit numbers (e.g., 123456789012).
    # Azure subscription IDs are unique identifiers that are GUIDs (Globally Unique Identifiers),
    # which are 32-character hexadecimal strings.
    cloud_account = models.CharField(max_length=32, null=False, blank=False)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return f'{self.name} ({self.unique_id})'
