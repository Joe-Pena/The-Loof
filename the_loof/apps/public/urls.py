from django.urls import path

from . import views

app_name = "public"
urlpatterns = [
    path("", views.ArticleList.as_view(), name="index"),
    path("article/<slug:slug>", views.article_detail, name="article_detail"),
    # path("comment/<slug:slug>", views.post_comment, name="post_comment"),
]
