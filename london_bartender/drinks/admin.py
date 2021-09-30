from django.contrib import admin

from london_bartender.drinks.models import Cocktail, Drink


@admin.register(Drink)
class DrinkAdmin(admin.ModelAdmin):
    list_display = ["id", "created_at"]
    search_fields = ["post"]


@admin.register(Cocktail)
class CocktailAdmin(admin.ModelAdmin):
    list_display = ["id", "classic", "created_at"]
    search_fields = ["drink"]
