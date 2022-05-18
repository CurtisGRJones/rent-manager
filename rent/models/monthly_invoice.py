from django.db import models

from rent.models.tenant import Tenant


class MonthlyInvoice(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.SET_NULL, null=True)
    tenant_name = models.CharField(max_length=33, null=False)
    amount = models.DecimalField(decimal_places=2, null=False)
    day_due = models.IntegerField(null=False)

    def save(
        self, *args, **kwargs
    ):
        self.tenant_name = f"{self.tenant.first_name} {self.tenant.last_name}"
        super().save(*args, **kwargs)


