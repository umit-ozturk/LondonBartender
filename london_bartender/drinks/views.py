from django.views.generic import ListView

from london_bartender.drinks.models import Post


class ClassicDrinksListView(ListView):
    model = Post

    def get_queryset(self):
        return self.get_queryset().filter(classic=True)
