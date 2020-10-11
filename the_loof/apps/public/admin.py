from django.contrib import admin
from .models import Article, Comment

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


class CommentAdmin(admin.ModelAdmin):
    list_display = ("username", "body", "article", "created", "active")
    list_filter = ("active", "created")
    search_fields = ("name", "body")
    actions = ["approve_comments"]

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)