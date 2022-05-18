from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from rent.models.unit import Unit


class Tenant(models.Model):
    first_name = models.CharField(max_length=16, null=False)
    last_name = models.CharField(max_length=16, null=False)
    current = models.BooleanField(null=False, default=True)
    rent = models.DecimalField(max_digits=7, decimal_places=2)
    apartment = models.ForeignKey(Unit, on_delete=models.SET_NULL, null=True)
    phone_number = PhoneNumberField(null=False)
    email = models.EmailField(null=False)

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.full_name()


