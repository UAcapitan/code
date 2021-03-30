from django.shortcuts import render
from .models import Article
from .forms import Article_Form

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

def edit(request):

    if request.method == 'POST':
        form = Article_Form(request.POST)
        if form.is_valid():
            form.save()

    context = {
        'list_articles': Article.objects.order_by('-id'),
        'form': Article_Form()
    }
    return render(request, 'main/edit_page.html', context)

def redact(request, article_id):
    context = {
        'list_artices': Article.objects.all(),
        'article_id': article_id
    }
    return render(request, 'main/redact.html', context)