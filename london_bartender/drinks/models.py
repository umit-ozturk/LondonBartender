from django.db import models
from django.utils.translation import gettext_lazy as _


class Post(models.Model):
    author = models.ForeignKey(
        "users.User",
        blank=True,
        related_name="drink_post",
        verbose_name=_("Author"),
        on_delete=models.CASCADE,
    )
    content = models.TextField(_("Drink content"))
    classic = models.BooleanField(_("Classic Drink"), default=False)
    created_at = models.DateTimeField(
        _("Created time"), auto_now_add=True, editable=False, null=True, blank=True
    )
    updated_at = models.DateTimeField(
        _("Updated time"), auto_now=True, editable=False, null=True, blank=True
    )

    class Meta:
        verbose_name = _("Drink Content")
        verbose_name_plural = _("Drink Contents")
        ordering = ("-created_at",)
