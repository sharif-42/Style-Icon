from django.contrib import admin
from .models import Product, ProductGroup, ProductType, ProductBrand
from common.admin import ProductBaseReadOnlyAdmin

# class BaseReadOnlyAdmin(admin.ModelAdmin):
#     readonly_fields = ["uuid", "created_at", "updated_at", "created_by", "updated_by", ]


@admin.register(Product)
class ProductModelAdmin(ProductBaseReadOnlyAdmin):
    list_display = ('name', 'code', 'product_group', 'product_type', 'brand', 'in_stock', 'is_serviceable')


@admin.register(ProductType)
class ProductTypeAdmin(ProductBaseReadOnlyAdmin):
    list_display = ('name', 'code', 'system_type', 'is_available')


@admin.register(ProductGroup)
class ProductGroupAdmin(ProductBaseReadOnlyAdmin):
    list_display = ('name', 'code', 'is_available')


@admin.register(ProductBrand)
class ProductBrandAdmin(ProductBaseReadOnlyAdmin):
    list_display = ('name', 'code', 'is_available')
