from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class Drink(models.Model):
    post = models.ForeignKey(
        "posts.Post",
        blank=True,
        related_name="drink_post",
        verbose_name=_("Post"),
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(
        _("Created time"),
        auto_now_add=True,
        editable=False,
        null=True,
        blank=True,
    )
    updated_at = models.DateTimeField(
        _("Updated time"), auto_now=True, editable=False, null=True, blank=True
    )

    class Meta:
        verbose_name = _("Drink")
        verbose_name_plural = _("Drinks")
        ordering = ("-created_at",)


class Cocktail(models.Model):
    drink = models.ForeignKey(
        "drinks.Drink",
        blank=True,
        related_name="drink",
        verbose_name=_("Drink"),
        on_delete=models.CASCADE,
    )
    slug = models.SlugField(_("Slug"), max_length=255, null=True)
    classic = models.BooleanField(_("Classic Drink"), default=False)
    created_at = models.DateTimeField(
        _("Created time"),
        auto_now_add=True,
        editable=False,
        null=True,
        blank=True,
    )
    updated_at = models.DateTimeField(
        _("Updated time"), auto_now=True, editable=False, null=True, blank=True
    )

    def get_absolute_url(self):
        return reverse(
            "drinks:cocktail_classic_detail", kwargs={"id": self.slug}
        )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.drink.post.title)
        super(Cocktail, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Cocktail")
        verbose_name_plural = _("Cocktails")
        ordering = ("-created_at",)
