from django.contrib import admin
from rent.models import Property, Unit


class UnitInline(admin.TabularInline):
    model = Unit
    show_change_link = True

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    fields = [
        'address',
        'city',
        'provence',
        'postal_code',
    ]

    list_display = [
        '__str__',
        'id',
    ]

    inlines = [UnitInline]
