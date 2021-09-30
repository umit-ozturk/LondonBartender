from django.views.generic import ListView

from london_bartender.drinks.models import Drink


class ClassicDrinksListView(ListView):
    model = Drink
    template_name = "drinks/drink_classic_list.html"

    def get_queryset(self):
        return super(ClassicDrinksListView, self).get_queryset().filter(classic=True)
