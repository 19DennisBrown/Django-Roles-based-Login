
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Permissions', {'fields': ('is_admin', 'is_user')}),
    )
    list_display = ('username', 'is_admin', 'is_user')

admin.site.register(CustomUser, CustomUserAdmin)
