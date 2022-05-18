from django.db import models

from rent.models.unit import Unit


class Tenant(models.Model):
    first_name = models.CharField(max_length=16, null=False)
    last_name = models.CharField(max_length=16, null=False)
    current = models.BooleanField(null=False)
    rent = models.DecimalField(decimal_places=2)
    apartment = models.ForeignKey(Unit, on_delete=models.SET_NULL, )

