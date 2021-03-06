from django.contrib import admin
from .models import Product, ProductGroup, ProductType, ProductBrand
from common.admin import ProductBaseReadOnlyAdmin


# class BaseReadOnlyAdmin(admin.ModelAdmin):
#     readonly_fields = ["uuid", "created_at", "updated_at", "created_by", "updated_by", ]


@admin.register(Product)
class ProductModelAdmin(ProductBaseReadOnlyAdmin):
    list_display = ('name', 'code', 'is_available', 'product_group', 'product_type',
                    'brand', 'in_stock', 'pre_order', 'is_serviceable', 'service_period')
    list_filter = ('is_serviceable', 'pre_order',)
    search_fields = ('code', 'name',)
    search_help_text = "search with name/code"  # new in django4.0, didn't work in older version


@admin.register(ProductType)
class ProductTypeAdmin(ProductBaseReadOnlyAdmin):
    list_display = ('name', 'code', 'system_type', 'is_available')


@admin.register(ProductGroup)
class ProductGroupAdmin(ProductBaseReadOnlyAdmin):
    list_display = ('name', 'code', 'is_available')


@admin.register(ProductBrand)
class ProductBrandAdmin(ProductBaseReadOnlyAdmin):
    list_display = ('name', 'code', 'is_available')
