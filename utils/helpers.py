import random

from the_loof.apps.public import models


def get_random_articles(exclude_id=None):
    max_article_index = models.Article.objects.last().id
    random_article_ids = []

    while len(random_article_ids) != 5:
        r_id = random.randint(1, max_article_index)

        if r_id != exclude_id:
            random_article_ids.append(r_id)

    return models.Article.objects.filter(id__in=random_article_ids)


def get_related_stocks(articles):
    stock_symbols = []

    for stock in articles:
        stock_symbols.append(stock["symbol"])

    return models.Stock.objects.filter(symbol__in=stock_symbols)


def get_random_stocks(offset=0, exclude_list=[]):
    exclude_set = set()
    for id in exclude_list:
        exclude_set.add(id)

    max_stock_index = models.Stock.objects.last().id
    random_range = []

    for id in range(1, max_stock_index + 1):
        if id not in exclude_set:
            random_range.append(id)

    random_stock_ids = random.sample(random_range, 4 - offset)

    return models.Stock.objects.filter(id__in=random_stock_ids)