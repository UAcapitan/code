from django.shortcuts import render
from . import models


def news(request):
    news = models.Articles.objects.all()
    return render(request, "news/news.html", {"news": news})

def create_news(request):
    return render(request, "news/create_news.html")