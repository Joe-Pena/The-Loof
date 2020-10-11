from django.urls import path

from . import views

app_name = "public"
urlpatterns = [
    path("", views.ArticleList.as_view(), name="index"),
    path("article/<slug:slug>", views.ArticleDetail.as_view(), name="article_detail"),
]