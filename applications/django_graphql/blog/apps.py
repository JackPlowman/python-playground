from django.apps import AppConfig


class BlogConfig(AppConfig):
    """Blog application configuration."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "blog"
