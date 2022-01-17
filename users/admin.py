from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


# Decorator
# Class 위에 있어야 한다.
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """Custom User Admin"""

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )
    # list_display = ("username", "gender", "language", "currency", "superhost")
    # list_filter = ("superhost", "language", "currency")


# admin.site.register(models.User, CustomUserAdmin)
# 위에 있는 Decorator랑 똑같은 코드
