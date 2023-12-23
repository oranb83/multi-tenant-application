from django.db import models

from api.models.resources.models import Resource
from api.models.tenants.models import Tenant


class Finding(models.Model):
    """
    Represents a finding in the system.

    @ivar external_id: The unique identifier for the finding.
    @type external_id: str

    @ivar type: The type of the finding.
    @type type: str

    @ivar title: The title of the finding.
    @type title: str

    @ivar severity: The severity level of the finding.
    @type severity: str

    @ivar created_at: The timestamp when the finding was created.
    @type created_at: datetime

    @ivar sensor: The sensor associated with the finding.
    @type sensor: str

    @ivar resource: The resource associated with the finding.
    @type resource: Resource

    @ivar tenant: The tenant associated with the finding.
    @type tenant: Tenant

    @ivar updated_at: The timestamp when the finding was last updated.
    @type updated_at: datetime

    @note: I've chosen to store the choices directly in the database to avoid repeated data
    conversion during serialization for each save and retrieve operation.
    Although this approach deviates from best practices, it ensures faster data access without
    serialization overhead. In scenarios requiring severity-based filters,
    a 'PositiveSmallIntegerField' could significantly enhance performance by storing this data
    as a small unsigned integer. However, since I currently don't implement filters based on
    severity and remain uncertain about its future implementation, I've prioritized expedited
    functionality over this conversion until such filters become necessary.
    """
    class SeverityChoices(models.TextChoices):
        CRITICAL = 'Critical', 'Critical'
        HIGH = 'High', 'High'
        MEDIUM = 'Medium', 'Medium'
        LOW = 'Low', 'Low'

    # Note:
    #   - Indexes will be added based on the queries that will be performed on the DB.
    #   - I was not sure if the meaining was that the external_id is the primary key or not,
    #     since I don't understand if an external_id can be shared with more than one tenant.
    #     Anyway, I decided to add a unique constraint on the tenant and external_id columns,
    #     since it makes sense to me.
    external_id = models.CharField(max_length=255, null=False, blank=False)
    type = models.CharField(max_length=255, null=False, blank=False)
    title = models.CharField(max_length=511, null=False, blank=True)  # titles can empty strings?
    severity = models.CharField(max_length=15, choices=SeverityChoices.choices, null=False,
                                blank=False)
    created_at = models.DateTimeField(null=False, blank=False)
    sensor = models.CharField(max_length=255, unique=True, null=False, blank=False)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, null=False, blank=False)
    # Not entirely sure it should be represented as a foreign key, but it makes sense to me
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, null=False, blank=False,
                               db_index=True)
    # Although not requested, it's important to add the updated_at column for
    # observability and debugging
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} ({self.external_id})'

    class Meta:
        unique_together = ('tenant', 'external_id')
