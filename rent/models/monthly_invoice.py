from django.db import models

from rent.models.tenant import Tenant


class MonthlyInvoice(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.SET_NULL, null=True)
    tenant_name = models.CharField(max_length=33, null=False)
    amount = models.DecimalField(max_digits=7, decimal_places=2, null=False)
    date_due = models.DateField()


    def save(
        self, *args, **kwargs
    ):
        self.tenant_name = f"{self.tenant.first_name} {self.tenant.last_name}"
        super().save(*args, **kwargs)



