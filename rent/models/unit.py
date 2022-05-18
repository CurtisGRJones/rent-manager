from django.db import models
from rent.models.property import Property


class Unit(models.Model):
    property = models.ForeignKey(Property, on_delete=models.SET_NULL, null=True)
    property_address = models.CharField(max_length=64, null=False)
    unit = models.CharField(max_length=10, null=False)

    def save(
        self, *args, **kwargs
    ):
        self.property_address = self.property.address
        super().save(*args, **kwargs)

