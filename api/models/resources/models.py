from django.db import models


class Resource(models.Model):
    """
    Represents a resource in the multi-tenant application.

    @ivar unique_id: The unique identifier of the resource.
    @type unique_id: str

    @ivar name: The name of the resource.
    @type name: str

    @ivar cloud_account: The cloud account associated with the resource.
    @type cloud_account: str

    @method __str__: Returns a string representation of the resource.

    @ivar Meta: Metadata for the resource.
    @type Meta: dict
    @ivar Meta.unique_together: Specifies the unique constraint for the resource.
    @type Meta.unique_together: tuple
    """

    unique_id = models.CharField(max_length=255, null=False, blank=False)
    name = models.CharField(max_length=255, null=False, blank=False)
    cloud_account = models.CharField(max_length=32, null=False, blank=False)

    def __str__(self):
        return f'{self.name} ({self.unique_id})'

    class Meta:
        unique_together = ('uniqueId', 'account')
