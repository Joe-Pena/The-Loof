from django.contrib import admin
from .models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        "headline",
        "slug",
        "article_type",
        "created",
    )
    list_filter = ("created",)
    search_fields = (
        "headline",
        "body",
        "instruments__symbol",
        "instruments__company_name",
        "byline",
    )
    prepopulated_fields = {"slug": ("headline",)}


admin.site.register(Article, ArticleAdmin)