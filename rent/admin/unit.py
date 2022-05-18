from django.contrib import admin
from rent.models import Unit, Tenant


class TenantInline(admin.TabularInline):
    model = Tenant
    show_change_link = True

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    fields = [
        'property',
        'unit',
    ]

    list_display = [
        '__str__',
        'property_address',
        'id',
    ]

    inlines = [TenantInline]
