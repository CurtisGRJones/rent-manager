from django.db import models
from localflavor.ca import models as ca_models


class Property(models.Model):
    address = models.CharField(max_length=64, null=False)
    city = models.CharField(max_length=16)
    provence = ca_models.CAProvinceField()
    postal_code = ca_models.CAPostalCodeField()

