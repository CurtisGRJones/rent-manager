from django.contrib import admin
from rent.models import Tenant


@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    fields = [
        'first_name',
        'last_name',
        'current',
        'rent',
        'apartment',
        'phone_number',
        'email',
    ]

    list_display = [
        '__str__',
        'apartment',
        'rent',
        'phone_number',
        'email',
        'id',
    ]
