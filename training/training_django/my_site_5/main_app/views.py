from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'main_app/index.html')

def articles(request):
    return render(request, 'articles/index.html')
