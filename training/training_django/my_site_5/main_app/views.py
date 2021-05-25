from django.shortcuts import render, HttpResponse
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ArticleForm

def index(request):
    return render(request, 'main_app/index.html')

def articles(request):
    return render(request, 'articles/index.html')

def form(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)

        if form.is_valid():
            return HttpResponseRedirect('')

    else:
        form = ArticleForm()

    return render(request, 'form/index.html', {'form': form})
