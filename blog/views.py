from django.shortcuts import render
from .models import *

def Home(request):
    blogs = Blog.objects.all()
    context = {'blogs':blogs}
    return render(request, 'blog/index.html', context)

def Detail(request, id):
    detail = Blog.objects.get(id=id)
    context = {'blog':detail}
    return render(request, 'blog/detail.html', context)
