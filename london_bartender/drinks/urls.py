from django.urls import path

from london_bartender.drinks.views import (
    ClassicCocktailsDetailView,
    ClassicCocktailsListView,
)

app_name = "drinks"

urlpatterns = [
    path(
        "cocktails/classics/",
        view=ClassicCocktailsListView.as_view(),
        name="cocktail_classic_list",
    ),
    path(
        "cocktails/classics/<int:pk>",
        view=ClassicCocktailsDetailView.as_view(),
        name="cocktail_classic_detail",
    ),
]
