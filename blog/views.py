import re
from django.shortcuts import render
from django.shortcuts import HttpResponse

def home(request):
    #return HttpResponse('hey there! Im django')
    return render(request,'home.html')

def about(request):
    #return HttpResponse('this is about page')
    return render(request,'about.html')