from django.contrib import admin
# from users.models import *

# # Register your models here.

# class UserAdmin(admin.ModelAdmin):
#     list_display = ('username', 'email')


# admin.site.register(User, UserAdmin)

from graphql_auth.models import UserStatus
admin.site.register(UserStatus)