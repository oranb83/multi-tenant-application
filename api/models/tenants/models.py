from django.db import models

class Tenant(models.Model):
    """
    Represents a tenant in the multi-tenant application.

    @ivar id: The unique identifier for the tenant.
    @type id: int
    """
    id = models.AutoField(primary_key=True)
    # Add other fields for the Tenant model here as needed
    # For example:
    # name = models.CharField(max_length=255)

    def __str__(self):
        return f'Tenant {self.id}'
