from django.contrib.syndication.views import Feed
from django.urls import reverse
from articles.models import Article


class BlogFeed(Feed):
    # config should be read from central file
    title = "Personal Web"
    link = "/blog/"
    description = "Updates from my personal blog."

    def items(self):
        return Article.objects.order_by("-pub_date")[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.get_snippet()

    def item_link(self, item):
        return reverse("articles:details", args=str(item.id))
