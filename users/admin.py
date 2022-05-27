import email
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser



class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('phone', 'email', 'is_superuser',)
    list_filter = ('is_superuser', 'is_staff',)
    fieldsets = (
        (None, {'fields': ('phone', 'password')}),
        ('Permissions', {'fields': ('is_superuser', 'is_staff',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'email', 'name', 'password1', 'password2', 'is_superuser', 'is_staff',)}
        ),
    )
    search_fields = ('phone',)
    ordering = ('phone',)

admin.site.register(CustomUser, CustomUserAdmin)

