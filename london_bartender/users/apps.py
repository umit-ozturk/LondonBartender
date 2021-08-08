from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "london_bartender.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import london_bartender.users.signals  # noqa F401
        except ImportError:
            pass
