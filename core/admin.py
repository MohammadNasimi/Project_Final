from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from core.models import User

UserAdmin.fieldsets = (
    (None, {'fields': ('phone', 'password')}),
    (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
    (_('Permissions'), {
        'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
    }),
    (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
)
UserAdmin.add_fieldsets = (
    (None, {
        'classes': ('wide',),
        'fields': ('phone', 'password1', 'password2'),
    }),
)
UserAdmin.list_display = ('phone', 'email', 'first_name', 'last_name', 'is_staff')
UserAdmin.search_fields = ('phone', 'first_name', 'last_name', 'email')

# Register your models here.
admin.site.register(User, UserAdmin)
