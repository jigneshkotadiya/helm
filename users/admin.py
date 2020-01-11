
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm
from .models import CusetomUser

class CustomUserAdmin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + (
            ("Extra", {'fields': ('is_student','is_teacher')}),
    )

    # fieldsets = (
    #     (None, {'fields': ('email', 'password', 'last_login')}),
    #     ('Permissions', {'fields': (
    #         'is_active', 
    #         'is_staff', 
    #         'is_superuser',
    #         'groups', 
    #         'user_permissions',
    #     )}),
    # )

    # list_display = ('email', 'is_staff', 'last_login')
    # list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    # search_fields = ('email',)
    # ordering = ('email',)
    # filter_horizontal = ('groups', 'user_permissions',)

admin.site.register(CusetomUser, CustomUserAdmin)
