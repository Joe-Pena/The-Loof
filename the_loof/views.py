from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def article(request):
    return render(request, "article.html")
