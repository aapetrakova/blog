from django.contrib import admin
from .models import UserPost


class UserPostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ['title']}


admin.site.register(UserPost, UserPostAdmin)