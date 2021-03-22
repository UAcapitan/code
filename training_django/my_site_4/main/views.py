from django.shortcuts import render
from .models import Article


def home(request):
    list_articles = Article.objects.all()
    context = {
        'name':'Ivan',
        'articles':list_articles,
    }
    return render(request, 'main/home.html', context)

def detail(request, article_id):
    article = Article.objects.get(id=article_id)
    context = {
        'article': article,
    }
    return render(request, 'main/detail.html', context)