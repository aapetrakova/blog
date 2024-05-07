from django.apps import AppConfig


class BlogConfig(AppConfig):
    """Config class for Blog app"""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
