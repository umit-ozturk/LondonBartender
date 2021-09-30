from django.views.generic import TemplateView

from london_bartender.posts.models import Post


class HomeView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data()
        context["post_list"] = Post.objects.all()
        return context
