from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Profile
from django.utils.translation import gettext_lazy as _

class CustomUserAdmin(UserAdmin):
    # Define the fields to be displayed in the admin panel for CustomUser
    model = CustomUser
    list_display = ('username', 'email', 'is_admin', 'is_user', 'is_active', 'date_joined')
    list_filter = ('is_admin', 'is_user', 'is_active')
    search_fields = ('username', 'email')
    ordering = ('username',)

    # Fields displayed in the form for creating or editing a user
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'groups', 'user_permissions')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_admin', 'is_user')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_admin', 'is_user'),
        }),
    )
    filter_horizontal = ('groups', 'user_permissions')  # Optional: for better UI on many-to-many relations

class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = ('user', 'bio', 'location')
    search_fields = ('user__username', 'user__email')
    list_filter = ('user__is_active',)

# Register CustomUser with the admin panel
admin.site.register(CustomUser, CustomUserAdmin)

# Register Profile model with the admin panel
admin.site.register(Profile, ProfileAdmin)
