from django.urls import path
from .views import articles_list_view,article_detail

urlpatterns = [
    path('wiki/articles', articles_list_view, name ='article_list' ),
    path('wiki/article/<int:pk>', article_detail, name='article_detail'),

]

# This might be needed, depending on your Django version
app_name = "wiki"