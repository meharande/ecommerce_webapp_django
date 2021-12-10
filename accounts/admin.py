from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model

from accounts.forms import (
    UserAdminCreationForm,
    UserAdminChangeForm,
)

User = get_user_model()

# Register your models here.
class UserAdmin(BaseUserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    list_display = ['id', 'first_name', 'last_name', 'email', 'phone', 'gender']
    search_fields = ['email', 'phone']
    list_filter = ['is_admin']
    ordering = ['email']
    filter_horizontal = ()

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ()}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name', 'last_name', 'email', 'phone', 'gender', 'password', 'confirm_password')}
         ),
    )

admin.site.register(User, UserAdmin)


