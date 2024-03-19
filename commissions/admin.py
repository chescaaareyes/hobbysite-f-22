from django.contrib import admin

from .models import Comment, Commission
  
class CommentAdmin(admin.ModelAdmin):
  model = Comment
  search_fields = ("entry", )

class CommentInline(admin.TabularInline):
  model = Comment
  
class CommissionAdmin(admin.ModelAdmin):
  model = Commission
  search_fields = ("title", )
  inlines = [CommentInline]
  
admin.site.register(Comment, CommentAdmin)
admin.site.register(Commission, CommissionAdmin)