# I did not implent the Tenant model and logic since it was not requested in the task
from django.db import models


class Tenant(models.Model):
    """
    Represents a tenant in the multi-tenant application.

    @ivar tenant_id: The unique identifier for the finding.
    @type tenant_id: int
    """
    id = models.IntegerField(primary_key=True)
    # Note: we will need to add more fields here in the future, such as name, etc.
    # name = models.CharField(max_length=255)

    # def __str__(self):
    #     return f'Tenant {self.tenant_id}'
