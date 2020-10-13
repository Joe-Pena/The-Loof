from django.http import request
from django.http.response import HttpResponseRedirect, JsonResponse
from the_loof.apps.public.forms import CommentForm
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.core import serializers

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
    # comment_form = CommentForm()

    # If posting comment
    if request.is_ajax and request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.article = article
            new_comment.save()

            return render(request, "comment.html", {"comment": new_comment})
    else:
        comment_form = CommentForm()

    # Get stock info
    max_stock_index = Stock.objects.last().id
    random_stock_ids = random.sample(range(1, max_stock_index + 1), 4)
    stock_list = Stock.objects.filter(id__in=random_stock_ids)

    # Get 5 random articles, excluding current
    curr_article_id = article.id
    max_article_index = Article.objects.last().id
    random_article_ids = []

    while len(random_article_ids) != 5:
        r_id = random.randint(1, max_article_index)

        if r_id != curr_article_id:
            random_article_ids.append(r_id)

    article_list = Article.objects.filter(id__in=random_article_ids)

    return render(
        request,
        template_name,
        {
            "article": article,
            "comments": comments,
            "new_comment": new_comment,
            "comment_form": comment_form,
            "stock_list": stock_list,
            "article_list": article_list,
        },
    )
