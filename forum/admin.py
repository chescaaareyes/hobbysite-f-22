from django.contrib import admin

from .models import Comment, Thread, ThreadCategory


class ThreadCategoryAdmin(admin.ModelAdmin):
    model = ThreadCategory


class ThreadAdmin(admin.ModelAdmin):
    model = Thread


class CommentAdmin(admin.ModelAdmin):
    model = Comment


admin.site.register(ThreadCategory, ThreadCategoryAdmin)
admin.site.register(Thread, ThreadAdmin)
admin.site.register(Comment, CommentAdmin)
