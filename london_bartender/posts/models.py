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
    title = models.CharField(_("Title"), null=True, blank=True, max_length=255)
    content = models.TextField(_("Content"))

    first_image = models.ImageField(
        _("First Image"), upload_to="images/posts", null=True, blank=True
    )

    second_image = models.ImageField(
        _("Second Image"), upload_to="images/posts", null=True, blank=True
    )

    third_image = models.ImageField(
        _("Third Image"), upload_to="images/posts", null=True, blank=True
    )

    featured = models.BooleanField(_("Featured Content"), default=False)

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
