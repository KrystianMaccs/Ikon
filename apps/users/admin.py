from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


class UserAdmin(BaseUserAdmin):
    list_display = [
        "id", "pkid", "username", "first_name", "last_name"]
    list_display_links = ["id", "pkid", "username"]



admin.site.register(User, UserAdmin)