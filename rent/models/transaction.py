from django.db import models
from rent.models import Tenant, Account


class Transaction(models.Model):
    paid_by = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    for_account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(
        max_length=16
        # TODO add choices
    )
    approved = models.BooleanField(default=False)