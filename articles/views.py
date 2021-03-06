from ast import arg
from django.shortcuts import render , HttpResponse
from tomlkit import date
from . import models

# Create your views here.

def articles_list(request):
    articles =  models.Article.objects.all().order_by('-date')
    args = {'articles':articles}
    return render(request,'articles/articles_list.html',args)

def article_detail(request,slug):
    # return HttpResponse(slug)
    article = models.Article.objects.get(slug=slug)
    args = {'article' : article}
    return render(request , 'articles/article_detail.html' , args)