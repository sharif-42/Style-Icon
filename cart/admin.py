from django.contrib import admin
from .models import Cart, CartLine


class CartLineInline(admin.TabularInline):
    model = CartLine
    can_delete = True
    extra = 1  # no of input form field
    fields = ["product_code", "product_name", "quantity", "price", "price_ex_vat",
              "total_amount", "total_amount_ex_vat"]


@admin.register(Cart)
class ProductModelAdmin(admin.ModelAdmin):
    inlines = [CartLineInline, ]
    list_display = ('uuid', 'customer', 'total_amount', 'total_amount_ex_vat', 'payment_type',)
    readonly_fields = ('uuid', 'created_at', 'updated_at',)
