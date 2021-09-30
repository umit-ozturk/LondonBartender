from django.db import models
from django.utils.translation import gettext_lazy as _


class Drink(models.Model):
    post = models.ForeignKey(
        "posts.Post",
        blank=True,
        related_name="drink_post",
        verbose_name=_("Post"),
        on_delete=models.CASCADE,
    )
    classic = models.BooleanField(_("Classic Drink"), default=False)
    created_at = models.DateTimeField(
        _("Created time"), auto_now_add=True, editable=False, null=True, blank=True
    )
    updated_at = models.DateTimeField(
        _("Updated time"), auto_now=True, editable=False, null=True, blank=True
    )

    class Meta:
        verbose_name = _("Drink")
        verbose_name_plural = _("Drinks")
        ordering = ("-created_at",)
