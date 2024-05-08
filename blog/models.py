from django.db import models
from django.urls import reverse
from django.utils import timezone

from user_management.models import Profile


class ArticleCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Article(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True, related_name="articles"
    )
    category = models.ForeignKey(
        ArticleCategory,
        on_delete=models.SET_NULL,
        null=True,
        related_name="articleCategory",
    )
    entry = models.TextField()
    headerImage = models.ImageField(upload_to="header_images/", blank=True, null=True)
    createdOn = models.DateTimeField(auto_created=True)
    updatedOn = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-createdOn"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_detail", args=[str(self.id)])


class Comment(models.Model):
    author = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True, related_name="comments"
    )
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="comments"
    )
    entry = models.TextField()
    createdOn = models.DateTimeField(default=timezone.now)
    updatedOn = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["createdOn"]

    def __str__(self):
        return f"Comment by {self.author} on {self.article}"
