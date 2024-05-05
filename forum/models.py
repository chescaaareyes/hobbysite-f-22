from django.db import models
from django.urls import reverse

from user_management.models import Profile


class ThreadCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return "{}".format(self.name)

    def get_absolute_url(self):
        return reverse("forum:forum_detail", args=[self.pk])

    class Meta:
        ordering = ["name"]


class Thread(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, related_name="thread_author", null=True
    )
    category = models.ForeignKey(
        ThreadCategory, on_delete=models.SET_NULL, related_name="categories", null=True
    )
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]


class Comment(models.Model):
    author = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, related_name="comment_author", null=True
    )
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name="threads")
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_on"]
