from django.db import models
from django.urls import reverse

# Create your models here.
class ArticleCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
      
class Article(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(
        ArticleCategory, 
        on_delete=models.SET_NULL, 
        null=True,
        related_name="article_category",
    )
    entry = models.TextField()
    created_on = models.DateTimeField(auto_created=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering  = ['-created_on']
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('article_details', args=[str(self.title)])