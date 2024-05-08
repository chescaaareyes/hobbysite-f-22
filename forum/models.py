from django.db import models

from user_management.models import Profile


class ThreadCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        ordering = ["name"]


class Thread(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        related_name="thread_author",
        null=True,
        editable=False,
    )
    category = models.ForeignKey(
        ThreadCategory, on_delete=models.SET_NULL, related_name="category", null=True
    )
    entry = models.TextField()
    image = models.ImageField(upload_to="images/", null=True)
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    updated_on = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        ordering = ["-created_on"]


class Comment(models.Model):
    author = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        related_name="comment_author",
        null=True,
        editable=False,
    )
    thread = models.ForeignKey(
        Thread, on_delete=models.CASCADE, related_name="thread", editable=False
    )
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_on"]
