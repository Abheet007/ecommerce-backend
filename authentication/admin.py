from  django.contrib.auth.models  import  Group
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User

# Register your models here.
class CustomUserAdmin(BaseUserAdmin):
    search_fields = [ 'email']  # Add the fields you want to search for

# Unregister the default UserAdmin


# Register the User model with your custom UserAdmin
admin.site.register(User)
admin.site.unregister(Group)