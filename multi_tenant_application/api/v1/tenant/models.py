from django.db import models


# I did not implent the Tenant model since it was not requested in the task
class Tenant(models.Model):
    tenant_id = models.IntegerField(primary_key=True)
    # Note: we will need to add more fields here in the future, such as name, etc.
