from the_loof.apps.public.forms import CommentForm
from django.shortcuts import get_object_or_404, render
from django.views import generic

import random

from .models import Article, Stock


class ArticleList(generic.ListView):
    queryset = Article.objects.filter(article_of_the_day=False).order_by("-created")
    template_name = "index.html"
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["featured_article"] = Article.objects.get(article_of_the_day=True)
        return context


def article_detail(request, slug):
    template_name = "article.html"
    article = get_object_or_404(Article, slug=slug)
    comments = article.comments.filter(active=True)
    new_comment = None

    # If posting comment
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.article = article
            new_comment.save()
    else:
        comment_form = CommentForm()

    # Get stock info
    max_index = Stock.objects.last().id
    random_ids = random.sample(range(max_index), 3)
    stock_list = Stock.objects.filter(id__in=random_ids)
    return render(
        request,
        template_name,
        {
            "article": article,
            "comments": comments,
            "new_comment": new_comment,
            "comment_form": comment_form,
            "stock_list": stock_list,
        },
    )