from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as CustomUserAdmin
from .models import CustomUser
# Register your models here.

@admin.register(CustomUser)
class CustomAdminUser(CustomUserAdmin):
    list_display = ['username','email','full_name','phone_number']