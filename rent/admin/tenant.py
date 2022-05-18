from django.contrib import admin
from rent.models import Tenant


@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    fields = [
        'first_name',
        'last_name',
        'phone_number',
        'email',
    ]

    list_display = [
        '__str__',
        'account',
        'phone_number',
        'email',
        'id',
    ]
