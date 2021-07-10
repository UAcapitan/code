from django.shortcuts import render, redirect
from .forms import ArticleForm
from .models import Article

def index(request):
    return render(request, 'main.html', {})

def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return render(request, 'error_form.html')
    else:
        form = ArticleForm()

        data = {
            'form': form
        }

        return render(request, 'create_article.html', data)

def articles(request):
    articles = Article.objects.all()
    
    data = {
        'articles':articles
    }

    return render(request, 'articles.html', data)

def post(request, id):
    article = Article.objects.get(id=id)

    data = {
        'article':article
    }

    return render(request, 'post.html', data)