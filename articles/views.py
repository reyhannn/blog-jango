from ast import arg
from django.shortcuts import render
from tomlkit import date
from . import models

# Create your views here.

def articles_list(request):
    articles =  models.Article.objects.all().order_by('date')
    args = {'articles':articles}
    return render(request,'articles/articles_list.html',args)