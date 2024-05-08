from django.contrib import admin

from .models import Comment, Thread, ThreadCategory


class CommentInline(admin.TabularInline):
    model = Comment


class ThreadCategoryAdmin(admin.ModelAdmin):
    model = ThreadCategory


class ThreadAdmin(admin.ModelAdmin):
    model = Thread
    inlines = [
        CommentInline,
    ]


admin.site.register(ThreadCategory, ThreadCategoryAdmin)
admin.site.register(Thread, ThreadAdmin)