from django.contrib import admin
from .models import Cart


@admin.register(Cart)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'customer', 'total_amount', 'total_amount_ex_vat', 'payment_type',)
    readonly_fields = ('uuid', 'created_at', 'updated_at',)
