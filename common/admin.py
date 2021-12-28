from django.contrib import admin


class ProductBaseReadOnlyAdmin(admin.ModelAdmin):
    readonly_fields = ["uuid", "created_at", "updated_at", "created_by", "updated_by", ]