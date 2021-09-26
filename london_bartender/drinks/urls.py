from django.urls import path

from london_bartender.drinks.views import ClassicDrinksListView

app_name = "drinks"

urlpatterns = [
    path("classics/", view=ClassicDrinksListView.as_view(), name="classic_drink_list"),
]
