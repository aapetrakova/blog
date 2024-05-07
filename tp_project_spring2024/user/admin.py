from django.contrib import admin
from .models import UserPost


class UserPostAdmin(admin.ModelAdmin):
    """Class for managing user post model"""
    prepopulated_fields = {'url': ['title']}


admin.site.register(UserPost, UserPostAdmin)