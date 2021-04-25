from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import Article
from django.urls import reverse

def index(request):
    latest_articles_list = Article.objects.order_by('-pub_date')[:5]
    return render(request, 'articles/list.html', {'latest_articles_list': latest_articles_list})

def detail(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
    except:
        raise Http404('Page not found')

    latest_comments_set = article.comment_set.order_by('-id')[:10]

    return render(request, 'articles/detail.html', {'article': article, 'latest_comments_set':latest_comments_set})

def leave_comment(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
    except:
        raise Http404('Page not found')
    
    article.comment_set.create(author_name=request.POST['name'], comment_text=request.POST['comment'])

    return HttpResponseRedirect(reverse('articles:detail', args=(article.id,)))