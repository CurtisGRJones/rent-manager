from django.db import models
from django_celery_beat.models import PeriodicTask, CrontabSchedule
from phonenumber_field.modelfields import PhoneNumberField

from rent.models.account import Account


class Tenant(models.Model):
    first_name = models.CharField(max_length=16, null=False)
    last_name = models.CharField(max_length=16, null=False)
    current = models.BooleanField(null=False, default=True)
    phone_number = PhoneNumberField(null=False)
    email = models.EmailField(null=False)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.full_name()


