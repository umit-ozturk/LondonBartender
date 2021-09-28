from django.db import models
from django.utils.translation import gettext_lazy as _


class Post(models.Model):
    author = models.ForeignKey(
        "users.User",
        blank=True,
        related_name="post",
        verbose_name=_("Author"),
        on_delete=models.CASCADE,
    )
    content = models.TextField(_("Content"))

    created_at = models.DateTimeField(
        _("Created time"), auto_now_add=True, editable=False, null=True, blank=True
    )
    updated_at = models.DateTimeField(
        _("Updated time"), auto_now=True, editable=False, null=True, blank=True
    )

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")
        ordering = ("-created_at",)
