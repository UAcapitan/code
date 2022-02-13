from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from . import forms
from . import models
from django.core.paginator import Paginator


def main(request):
    articles = models.Article.objects.all().order_by('-id')
    articles_paginator = Paginator(articles, 3)
    page_number = request.GET.get('page')
    page_obj = articles_paginator.get_page(page_number)

    last_rec = None
    try:
        last_rec = models.Recommendation.objects.get(pk=1)
    except:
        pass

    context = {
        'articles':page_obj,
        'page_obj':page_obj,
        'last_rec':last_rec
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
    token = ''
    try:
        avatar = models.Avatar.objects.get(user=request.user)
    except:
        avatar = None
    context = {
        'token': token,
        'avatar': avatar
    }
    return render(request, 'appmain/profile.html', context=context)

def article(request, id):
    article = models.Article.objects.get(id=id)
    rec = models.Article.objects.all().order_by('-id')[:3]
    if request.method == 'POST':
        temp = request.POST.copy()
        temp['article'] = article
        if request.user.is_authenticated:
            username = request.user
        else:
            username = 'Anonymous'
        temp['user'] = username
        form = forms.CommentsForm(temp)
        if form.is_valid():
            form.save()
    form = forms.CommentsForm()
    comments = models.Comment.objects.filter(article_id=id)
    user = request.user
    like = True if len(models.Like.objects.filter(article=article, user=user)) > 0 else False
    context = {
        'article': article,
        'articles': rec,
        'form': form,
        'comments': comments,
        'like': like
    }
    return render(request, 'appmain/article.html', context=context)

def add_in_favourite(request, id):
    username=request.user.username
    if models.Favourite.objects.filter_by(username=username, id_article=id) == None:
        models.Favourite(username=username, id_article=id).save()
        text='You liked this'
    else:
        text='You liked this some early'
    return redirect('favourite')

def favourite(request):
    user = request.user
    articles = models.Like.objects.filter(user=user).order_by('-id')
    articles_paginator = Paginator(articles, 15)
    page_number = request.GET.get('page')
    page_obj = articles_paginator.get_page(page_number)
    context = {
        'articles':page_obj,
        'page_obj':page_obj,
    }
    return render(request, 'appmain/favourite.html', context=context)

def rate(request):
    articles = models.Article.objects.all().order_by('-likes')[:10]
    context = {
        'articles': articles
    }
    return render(request, 'appmain/rate.html', context=context)

def list_of_articles(request):
    articles = models.Article.objects.all().order_by('-id')
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
            form = forms.ArticleForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('admin_page')
            print(form.is_valid())
        else:
            form = forms.ArticleForm()
        context = {
            'form':form,
        }
        return render(request, 'appmain/add_article.html', context=context)

def set_recommendation(request, id):
    if request.user.is_staff:
        last_rec = None
        try:
            last_rec = models.Recommendation.objects.get(pk=1)
        except:
            pass
        if last_rec:
            last_rec.delete()
        models.Recommendation(id=1, article=models.Article.objects.get(id=id)).save()
        return redirect('main')

def admin_page(request):
    if request.user.is_staff:
        return render(request, 'appmain/admin_page.html')

def admin_articles(request):
    if request.user.is_staff:
        articles = models.Article.objects.all().order_by('-id')
        articles_paginator = Paginator(articles, 15)
        page_number = request.GET.get('page')
        page_obj = articles_paginator.get_page(page_number)
        context = {
            'articles': page_obj,
            'page_obj': page_obj
        }
        return render(request, 'appmain/admin_articles.html', context=context)

def article_edit(request, id):
    if request.user.is_staff:
        try:
            model = models.Article.objects.get(pk=id)
        except:
            pass
        if request.method == 'POST':
            form = forms.ArticleForm(request.POST, request.FILES, instance=model)
            if form.is_valid():
                form.save()
                return redirect('admin_articles')
        else:
            form = None
            try:
                form = forms.ArticleForm(instance=model)
            except:
                pass
            context = {
                'form': form
            }
        return render(request, 'appmain/article_edit.html', context=context)

def article_delete(request, id):
    if request.user.is_staff:
        try:
            article = models.Article.objects.get(id=id)
            article.delete()
        except:
            pass
        return redirect('admin_articles')

def like(request, id):
    if request.user.is_authenticated:
        article = models.Article.objects.get(id=id)
        user = request.user
        like = models.Like.objects.filter(article=article, user=user)
        if len(like) > 0:
            models.Like.objects.get(article=article, user=user).delete()
            article.likes -= 1
        else:
            models.Like(article=article, user=user).save()
            article.likes += 1
        article.save()
        return redirect('article', id=id)

def settings(request):
    form_set_avatar = forms.AvatarForm()
    context = {
        'form_avatar': form_set_avatar,
    }
    return render(request, 'appmain/settings.html', context=context)

def set_avatar(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            print(request.POST)
            temp = request.POST.copy()
            temp['user'] = request.user
            form = forms.AvatarForm(temp, request.FILES)
            if form.is_valid():
                if models.Avatar.objects.filter(user=request.user):
                    models.Avatar.objects.get(user=request.user).delete()
                form.save()
                return redirect('profile')
    return redirect('main')