from django.db import models


class Resource(models.Model):
    unique_id = models.CharField(max_length=255, null=False, blank=False)
    name = models.CharField(max_length=255, null=False, blank=False)
    # According to a Google search:
    #   * The maximum length of an AWS account number is 12 digits
    #   * Them maximum length of an Azure subscription ID is 32 characters
    # Note:
        # I'm not sure in this context what is the tenant id,
        # I assume that it's the account?
    cloud_account = models.CharField(max_length=32, null=False, blank=False)

    def __str__(self):
        return f'{self.name} ({self.unique_id})'

    class Meta:
        unique_together = ('uniqueId', 'account')
