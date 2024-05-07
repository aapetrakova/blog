from django.apps import AppConfig


class UserConfig(AppConfig):
    """Class representing the app config"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user'
