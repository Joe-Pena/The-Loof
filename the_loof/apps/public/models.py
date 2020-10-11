from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Article(models.Model):
    headline = models.CharField(max_length=200, unique=True, blank=False, null=False)
    slug = models.SlugField(max_length=200, unique=True, blank=False, null=False)
    authors = models.JSONField(default=dict, blank=True)
    article_type = models.CharField(
        max_length=200, unique=False, blank=False, null=False
    )
    promo = models.CharField(max_length=200, default="")
    disclosure = models.TextField()
    body = models.TextField(blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    instruments = models.JSONField(default=dict, blank=True)
    bureau = models.JSONField(default=dict, blank=True)
    collection = models.JSONField(default=dict, blank=True)
    tags = models.JSONField(default=dict, blank=True)
    recommendations = models.JSONField(default=dict, blank=True)
    images = models.JSONField(default=dict, blank=True)
    video = models.CharField(max_length=200, blank=True, null=True)
    pitch = models.JSONField(default=dict, blank=True)
    links = models.JSONField(default=dict, blank=True)
    byline = models.CharField(max_length=200, default="", blank=False, null=False)
    visibility = models.IntegerField(default=100)
    publish_at = models.DateTimeField(auto_now=True)
    static_page = models.BooleanField(default=False)
    author_override = models.BooleanField(null=True)
    uuid = CharField(max_length=200, default="")
    product_id = models.IntegerField(default=0)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.headline