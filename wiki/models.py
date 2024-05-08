from django.db import models
from django.urls import reverse

from user_management.models import Profile


class ArticleCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Article(models.Model):
    author = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True, related_name="author"
    )
    title = models.CharField(max_length=255)
    category = models.ForeignKey(
        "ArticleCategory",
        on_delete=models.SET_NULL,
        null=True,
        related_name="article_category",
    )
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, null=True)
    image = models.ImageField(upload_to="article_images/", null=True, blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("wiki:article_detail", args=[int(self.pk)])


class Comment(models.Model):
    author = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True, related_name="user_comments"
    )
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        null=True,
        related_name="article_comments",
    )
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.author.user} for {self.article.title}"
