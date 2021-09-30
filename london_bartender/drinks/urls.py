from django.urls import path

from london_bartender.drinks.views import ClassicCocktailsListView

app_name = "drinks"

urlpatterns = [
    path(
        "cocktails/classics/",
        view=ClassicCocktailsListView.as_view(),
        name="cocktail_classic_list",
    ),
]
