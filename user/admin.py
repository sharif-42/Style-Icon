from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from user.models import User, UserLoginLog


class UserAdmin(BaseUserAdmin):
    ordering = ["-id"]
    list_display = ('username', 'email', 'is_staff', 'is_blocked', 'is_active', 'is_pending', 'is_dashboard_user')
    list_filter = ('is_active', 'is_staff', 'is_dashboard_user', 'is_blocked', 'is_pending')
    readonly_fields = ('joined_date', 'last_login',)

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': (
            'phone_number', 'email', 'first_name', 'mid_name', 'last_name', 'is_staff',
            'is_active', 'is_blocked', 'is_dashboard_user', 'is_pending',
        )
        }),
        ('Permissions', {'fields': ('user_permissions', 'groups')}),
        ('Important dates', {'fields': ('last_login', 'updated_at', 'joined_date')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2')
        }),
        ('Personal info', {
            'fields': ('email', 'phone_number', 'first_name', 'mid_name', 'last_name',
                       'is_dashboard_user', 'is_pending',)
        })
    )


class UserLoginLogModelAdmin(admin.ModelAdmin):
    list_display = ("used_user_name", "used_email", "is_successful")
    list_filter = ("is_successful",)
    readonly_fields = ("used_user_name", "attempted_time", "ip_address")


admin.site.register(User, UserAdmin)
admin.site.register(UserLoginLog, UserLoginLogModelAdmin)
