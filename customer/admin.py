from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Company


class CustomerAdmin(UserAdmin):
    pass

admin.site.register(User, CustomerAdmin)
admin.site.register(Company)