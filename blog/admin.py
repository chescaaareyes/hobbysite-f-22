from django.contrib import admin
from .models import Article, ArticleCategory

# Register your models here.

class ArticleCategoryAdmin(admin.ModelAdmin):
    model = ArticleCategory


class ArticleAdmin(admin.ModelAdmin):
    model = Article

admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleCategory, ArticleCategoryAdmin)