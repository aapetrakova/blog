from django.contrib import admin
from .models import UserPost, Profile


class UserPostAdmin(admin.ModelAdmin):
    """Class for managing user post model"""
    prepopulated_fields = {'url': ['title']}


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'birth_date', 'slug')
    list_display_links = ('user', 'slug')


admin.site.register(UserPost, UserPostAdmin)
admin.site.register(Profile, ProfileAdmin)