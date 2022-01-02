from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from . import forms
from django.contrib.auth.forms import AuthenticationForm
from . import models
from django.core.paginator import Paginator


def main(request):
    articles = models.Article.objects.all()
    articles_paginator = Paginator(articles, 3)
    page_number = request.GET.get('page')
    page_obj = articles_paginator.get_page(page_number)
    context = {
        'articles':page_obj,
        'page_obj':page_obj,
    }
    return render(request, 'appmain/main.html', context=context)

def reg(request):
    if request.method == "POST":
        form = forms.NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("main")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = forms.NewUserForm()
    return render(request, 'appmain/registration.html', {"register_form":form})

def login_view(request):
    if request.method == "POST":
        form = forms.AuthForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("main")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = forms.AuthForm()
    return render(request, "appmain/login.html", {"login_form":form})

def logout_view(request):
    logout(request)
    messages.info(request, "You have successfully logged out.") 
    return redirect("main")

def profile(request):
    return render(request, 'appmain/profile.html')

def article(request, id):
    return render(request, 'appmain/article.html')

def favourite(request):
    return render(request, 'appmain/favourite.html')

def rate(request):
    return render(request, 'appmain/rate.html')

def list_of_articles(request):
    articles = models.Article.objects.all()
    articles_paginator = Paginator(articles, 7)
    page_number = request.GET.get('page')
    page_obj = articles_paginator.get_page(page_number)
    context = {
        'articles':page_obj,
        'page_obj':page_obj,
    }
    return render(request, 'appmain/list_of_articles.html', context=context)

def add_article(request):
    if request.user.is_staff:
        if request.method == 'POST':
            form = forms.ArticleForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('admin_page')
        else:
            form = forms.ArticleForm()
        context = {
            'form':form,
        }
        return render(request, 'appmain/add_article.html', context=context)

def recommendation(request):
    return render(request, 'appmain/recommendation.html')

def set_recommendation(request):
    if request.method == 'POST':
        if request.user.is_staff:
            if request.method == 'POST':
                form = forms.ArticleForm(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('admin_page')
            else:
                form = forms.ArticleForm()
        context = {
            'form':form,
        }
        return redirect('recommendation')
    return render(request, 'appmain/set_recommendation.html')

def admin_page(request):
    if request.user.is_staff:
        return render(request, 'appmain/admin_page.html')