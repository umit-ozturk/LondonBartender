from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DrinksConfig(AppConfig):
    name = "london_bartender.drinks"
    verbose_name = _("Drinks")

    def ready(self):
        try:
            import london_bartender.drinks.signals  # noqa F401
        except ImportError:
            pass
