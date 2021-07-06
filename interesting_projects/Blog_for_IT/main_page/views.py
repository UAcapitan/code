from django.shortcuts import render

def index(request):
    return render(request, 'main.html', {})

def create_article(request):
    return render(request, 'create_article.html', {})


