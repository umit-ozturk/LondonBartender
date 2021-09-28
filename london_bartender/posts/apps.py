from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PostsConfig(AppConfig):
    name = "london_bartender.posts"
    verbose_name = _("Posts")

    def ready(self):
        try:
            import london_bartender.posts.signals  # noqa F401
        except ImportError:
            pass
