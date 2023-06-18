from django.contrib import admin
from users.models import (
    Profile
)

class CustomAdmin(admin.ModelAdmin):
    model = Profile
    list_display = [
        # "first_name",
        # "last_name",
        "user",
        "pk",
    ]

admin.site.register(Profile, CustomAdmin)