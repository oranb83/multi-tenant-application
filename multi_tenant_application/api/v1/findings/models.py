from django.db import models

from api.v1.resource.models import Resource
from api.v1.tenant.models import Tenant


class Finding(models.Model):
    # Note: I'm saving the choices, in the DB, as I get them to avoid the need to convert the data
    # in the serializer upon each save and retrieve. I'm aware that this is not the best practice
    # and if the task requested me also to support filters based on severity then there is no doubt
    # that I would use a "PositiveSmallIntegerField" and save this column as a small unsigned int,
    # which is much more effient when using a B-Tree index and impact performance.
    # Since I'm not implementating any filters on the severity column, and I'm not sure if I will,
    # at the moment, not adding this conversation is faster at this point until such filter will be
    # added.
    class SeverityChoices(models.TextChoices):
        CRITICAL = 'Critical', 'Critical'
        HIGH = 'High', 'High'
        MEDIUM = 'Medium', 'Medium'
        LOW = 'Low', 'Low'

    # Indexes will be added based on the queries that will be performed on the DB.
    external_id = models.CharField(max_length=255, primary_key=True)
    type = models.CharField(max_length=255, null=False, blank=False)
    title = models.CharField(max_length=511, null=False, blank=True)  # titles can empty strings?
    severity = models.CharField(max_length=15, choices=SeverityChoices.choices, null=False,
                                blank=False)
    created_at = models.DateTimeField(null=False, blank=False)
    sensor = models.CharField(max_length=255, unique=True, null=False, blank=False)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, null=False, blank=False)
    tenant_id = models.ForeignKey(Tenant, on_delete=models.CASCADE, null=False, blank=False)
    # Although not requested, it's important to add the updated_at column for
    # observability and debugging
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} ({self.external_id})'

    class Meta:
        unique_together = ('tenant_id', 'external_id')
