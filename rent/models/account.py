from django.db import models
from django_celery_beat.models import PeriodicTask, CrontabSchedule
from rent.models.unit import Unit


class Account(models.Model):
    rent = models.DecimalField(max_digits=7, decimal_places=2)
    apartment = models.ForeignKey(Unit, on_delete=models.SET_NULL, null=True)
    billing_period = models.ForeignKey(CrontabSchedule, on_delete=models.SET_NULL, null=True, blank=True)
    periodic_billing_job = models.ForeignKey(PeriodicTask, on_delete=models.SET_NULL, null=True, blank=True)
    closed = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.billing_period is not None:
            if self.periodic_billing_job is None:
                self.periodic_billing_job = PeriodicTask()
            self.periodic_billing_job.name = f'Generate Bill for Account [{self.id}]'
            self.periodic_billing_job.crontab = self.billing_period
            self.periodic_billing_job.task = 'generate_bill'
            self.periodic_billing_job.kwargs = {
                'tenant_id': self.id,
            }
            self.periodic_billing_job.save(*args, **kwargs)
        super().save(*args, **kwargs)