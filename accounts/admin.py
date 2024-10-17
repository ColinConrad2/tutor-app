#accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Class
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    list_display = [
        "email",
        "username",
        "age",
        "pronouns",          # NEW
        "tutoring_hours",     # NEW
        "is_staff",           #NEW
    ]

    # viewing and editing an existing user
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("age", "pronouns", "tutoring_hours", "ta_classes")}),
    )

    # for adding a new user
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("age", "pronouns", "tutoring_hours", "ta_classes")}),
    )

    filter_horizontal = ('ta_classes',)  # For the ManyToMany relationship with classes

# updated CustomUserAdmin
admin.site.register(CustomUser, CustomUserAdmin)

#class model
admin.site.register(Class)