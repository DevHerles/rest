from django.contrib import admin
from apps.users.models import User
from django.contrib.auth.admin import UserAdmin


class UserAdminConfig(UserAdmin):
    model = User
    search_fields = (
        'email',
        'username',
        'first_name',
    )
    list_filter = ('email', 'username', 'first_name', 'is_active', 'is_staff')
    ordering = ('id', )
    list_display = ('id', 'email', 'username', 'first_name', 'is_active',
                    'is_staff')
    fieldsets = (
        (None, {
            'fields': (
                'email',
                'username',
                'first_name',
            )
        }),
        ('Permissions', {
            'fields': ('is_staff', 'is_active')
        }),
    )


admin.site.register(User, UserAdminConfig)
