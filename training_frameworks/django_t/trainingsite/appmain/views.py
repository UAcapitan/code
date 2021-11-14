from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *

menu = ['Main page', 'Articles', 'About']

def index(request):
    articles = Article.objects.all()
    return render(request, 'appmain/index.html', {'title':'Main page', 'menu':menu, 'articles':articles})

def article(request, id):
    if (request.GET):
        print(request.GET)

    if (request.POST):
        print(request.POST)

    return render(request, 'appmain/article.html', {'title':'Article', 'menu':menu})

def year(request, year):
    if int(year) > 2021:
        raise Http404()
    if int(year) > 2000:
        return redirect('main')
    if int(year) > 1990:
        return redirect('main', permanent=True)
    return HttpResponse(f'<h1>Year {str(year)}</h1>')

def articles(request):
    articles = Article.objects.all()
    context = {
        'articles':articles
    }
    return render(request, 'appmain/articles.html', context)

def show_category(request, id):
    category = Category.objects.get(pk=id)
    articles = Article.objects.filter(cat=id)
    if len(articles) == 0:
        raise Http404()
    return render(request, 'appmain/category.html', {'category':category, 'articles':articles})

def pageNotFound(request, exception):
    return HttpResponseNotFound(f'<h1>Page not found</h1>')
