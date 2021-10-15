from django.core.paginator import Paginator
from django.views.generic import TemplateView

from london_bartender.drinks.models import Cocktail
from london_bartender.posts.models import Post


class HomeView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data()
        context["classic_cocktail_list"] = Paginator(
            Cocktail.objects.filter(classic=True), 4
        ).get_page("1")
        context["featured_post_list"] = Post.objects.filter(featured=True)[:3]
        return context
