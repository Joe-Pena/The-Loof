from django.db import models, transaction

# Create your models here.
# Article model is full of JSONfields merely
# for convinience. It was the most speedy approach
# for this ocassion, while maintaining the ability
# to query the data.
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
    uuid = models.CharField(max_length=200, default="")
    product_id = models.IntegerField(default=0)
    article_of_the_day = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.headline

    # Override save method in order to make
    # `article_of_the_day` property a unique
    # boolean (Only one article can be True)
    def save(self, *args, **kwargs):
        if not self.article_of_the_day:
            return super(Article, self).save(*args, **kwargs)
        with transaction.atomic():
            Article.objects.filter(article_of_the_day=True).update(
                article_of_the_day=False
            )
            return super(Article, self).save(*args, **kwargs)


# Simple comment model, it maps to an article
# through it's foreign key
class Comment(models.Model):
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="comments"
    )
    username = models.CharField(max_length=80, default="Anonymous User")
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    # Active field in the case of spam coming in.
    # Not currently in use, but a filtering function
    # could be implemented later on.
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f"Comment {self.body} by {self.username}"


# From stock fixture, only took what I believed to be
# necessary for this assignment
class Stock(models.Model):
    company_name = models.CharField(max_length=50, blank=False, null=False)
    symbol = models.CharField(max_length=10, blank=False, null=False)
    exchange = models.CharField(max_length=10, blank=False, null=False)
    exchange_name = models.CharField(max_length=50, blank=False, null=False)
    instrument_id = models.IntegerField()
    change = models.FloatField()
    current_price = models.FloatField()
    percent_change = models.FloatField()
    website = models.URLField()
