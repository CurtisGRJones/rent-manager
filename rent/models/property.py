from django.db import models
# TODO update this when 4.0 gets released https://github.com/django/django-localflavor
from packages.django_localflavor.localflavor.ca import models as ca_models


class Property(models.Model):
    address = models.CharField(max_length=64, null=False)
    city = models.CharField(max_length=16)
    provence = ca_models.CAProvinceField()
    postal_code = ca_models.CAPostalCodeField()

    def __str__(self):
        return f'{self.address}, {self.city}, {self.provence}, {self.postal_code}'

    class Meta:
        verbose_name_plural = 'Properties'
