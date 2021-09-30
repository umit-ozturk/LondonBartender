from django.urls import path

from london_bartender.drinks.views import ClassicCocktailsListView

app_name = "drinks"

urlpatterns = [
    path(
        "classics/", view=ClassicCocktailsListView.as_view(), name="classic_drink_list"
    ),
]
