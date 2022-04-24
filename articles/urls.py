from unicodedata import name
from django.urls import path
from . import views

app_name = 'acticles'

urlpatterns = [
    path('' , views.articles_list , name = 'listOfArticles'),
    path('<slug>' , views.article_detail , name='detail'),
]
