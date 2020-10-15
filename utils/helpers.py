def get_related_stocks(articles):
    stock_list = []

    for stock in articles:
        stock_list.append(stock["symbol"])

    return stock_list