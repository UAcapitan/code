from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models, forms
from django.views.generic import DetailView, UpdateView, DeleteView


def news(request):
    news = models.Articles.objects.order_by("-date")
    return render(request, "news/news.html", {"news": news})

def create_news(request):
    if request.method == "POST":
        form = forms.ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("news")
        else:
            return HttpResponse("Wrong form data")
    return render(request, "news/create_news.html", {"form": forms.ArticleForm()})

class NewsDetailView(DetailView):
    model = models.Articles
    template_name = "news/details_view.html"
    context_object_name = "article"

class NewsUpdateView(UpdateView):
    model = models.Articles
    template_name = "news/create_news.html"
    form_class = forms.ArticleForm

class NewsDeleteView(DeleteView):
    model = models.Articles
    success_url = "/news/"
    template_name = "news/news_delete.html"