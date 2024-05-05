from django.contrib import admin

from .models import Thread, ThreadCategory


class ThreadCategoryAdmin(admin.ModelAdmin):
    model = ThreadCategory


class ThreadAdmin(admin.ModelAdmin):
    model = Thread


admin.site.register(ThreadCategory, ThreadCategoryAdmin)
admin.site.register(Thread, ThreadAdmin)
