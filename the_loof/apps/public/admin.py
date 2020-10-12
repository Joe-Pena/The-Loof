from django.contrib import admin
from .models import Article, Comment, Stock

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("headline", "slug", "article_type", "created", "article_of_the_day")
    list_filter = ("created",)
    search_fields = (
        "headline",
        "body",
        "instruments__symbol",
        "instruments__company_name",
        "byline",
    )
    prepopulated_fields = {"slug": ("headline",)}


class CommentAdmin(admin.ModelAdmin):
    list_display = ("username", "body", "article", "created", "active")
    list_filter = ("active", "created")
    search_fields = ("name", "body")
    actions = ["approve_comments"]

    # TODO: The idea here is that there's
    # a function which will regex target words
    # and if found, set active to False.
    def approve_comments(self, request, queryset):
        queryset.update(active=True)


class StockAdmin(admin.ModelAdmin):
    list_display = ("company_name", "symbol", "exchange")
    list_filter = ("exchange",)
    search_fields = ("company_name", "symbol", "exchange")


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Stock, StockAdmin)
