from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls.base import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import *
from .forms import *

menu = ['Main page', 'Articles', 'About']

class ArticleMain(ListView):
    model = Article
    template_name = 'appmain/index.html'
    context_object_name = 'articles'

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Main page'
        return context

    def get_queryset(self):
        return Article.objects.filter(is_published=True)

# def index(request):
#     articles = Article.objects.all()
#     context = {
#         'title':'Main page', 
#         'menu':menu,
#         'articles':articles
#     }
#     return render(request, 'appmain/index.html', context)

# def article(request, id):
#     art = get_object_or_404(Article, slug=id)
#     if (request.GET):
#         print(request.GET)

#     if (request.POST):
#         print(request.POST)

#     context = {
#         'title':'Article', 
#         'menu':menu,
#         'art':art
#     }

#     return render(request, 'appmain/article.html', context)

def year(request, year):
    if int(year) > 2021:
        raise Http404()
    if int(year) > 2000:
        return redirect('main')
    if int(year) > 1990:
        return redirect('main', permanent=True)
    return HttpResponse(f'<h1>Year {str(year)}</h1>')

class ShowPage(DetailView):
    model = Article
    template_name = 'appmain/article.html'
    context_object_name = 'art'
    allow_empty = False

def articles(request):
    articles = Article.objects.all()
    context = {
        'articles':articles
    }
    return render(request, 'appmain/articles.html', context)

class CategoryPage(ListView):
    model = Category
    template_name = 'appmain/category.html'
    context_object_name = 'cats'
    allow_empty = False

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Category'
        return context

    def get_queryset(self):
        return Article.objects.filter(cat__slug=self.kwargs['id'],is_published=True)

# def show_category(request, id):
#     category = Category.objects.get(slug=id)
#     print(category.id)
#     articles = Article.objects.filter(cat=category.id)
#     if len(articles) == 0:
#         raise Http404()
#     return render(request, 'appmain/category.html', {
#         'category':category,
#         'articles':articles
#     })

class FormPage(CreateView):
    form_class = AddForm
    template_name = 'appmain/form_page.html'
    success_url = reverse_lazy('main')

# def form_page(request):
#     if request.method == 'POST':
#         form = AddForm(request.POST, request.FILES)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             form.save()
#             return redirect('main')
#     else:
#         form = AddForm()
#     return render(request, 'appmain/form_page.html', {'form':form})

def pageNotFound(request, exception):
    return HttpResponseNotFound(f'<h1>Page not found</h1>')