from django.contrib import admin

from london_bartender.drinks.models import Drink


@admin.register(Drink)
class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "post", "classic", "updated_at"]
    search_fields = ["author"]
