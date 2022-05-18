from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# TODO update this when 4.0 gets released https://github.com/django/django-localflavor
from packages.django_localflavor.localflavor.ca import models as ca_models


class Property(models.Model):
    address = models.CharField(max_length=64, null=False)
    city = models.CharField(max_length=16)
    provence = ca_models.CAProvinceField()
    postal_code = ca_models.CAPostalCodeField()
    phone_number = PhoneNumberField(null=False)

