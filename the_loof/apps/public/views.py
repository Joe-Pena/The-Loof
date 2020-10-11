from django.shortcuts import render
from django.views import generic

from .models import Article


def index(request):
    return render(request, "index.html")


def article(request):
    return render(request, "article.html")


class ArticleList(generic.ListView):
    queryset = Article.objects.order_by("-created")
    template_name = "index.html"


class ArticleDetail(generic.DetailView):
    model = Article
    template_name = "article.html"
