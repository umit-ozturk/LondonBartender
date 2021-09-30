from django.views.generic import ListView

from london_bartender.drinks.models import Cocktail


class ClassicCocktailsListView(ListView):
    model = Cocktail
    template_name = "drinks/cocktail_classic_list.html"

    def get_queryset(self):
        return super(ClassicCocktailsListView, self).get_queryset().filter(classic=True)
