from django.contrib import admin
from rent.models import Tenant, Account


class TenantInline(admin.TabularInline):
    model = Tenant
    show_change_link = True

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    fields = [
        'rent',
        'apartment',
        'billing_period',
        'closed'
    ]

    list_display = [
        '__str__',
    ]

    inlines = [
        TenantInline,
    ]
