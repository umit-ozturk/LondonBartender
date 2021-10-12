from django.core.paginator import Paginator
from django.views.generic import TemplateView

from london_bartender.posts.models import Post


class HomeView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data()
        context["post_list"] = Paginator(Post.objects.all(), 4).get_page("1")
        context["featured_post_list"] = Post.objects.filter(featured=True)[:3]
        return context
