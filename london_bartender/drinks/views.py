from django.views.generic import DetailView, ListView

from london_bartender.drinks.models import Cocktail


class ClassicCocktailsListView(ListView):
    model = Cocktail
    template_name = "drinks/cocktail_classic_list.html"
    paginate_by = 4

    def get_queryset(self):
        return super(ClassicCocktailsListView, self).get_queryset().filter(classic=True)


class CocktailDetailView(DetailView):
    model = Cocktail
