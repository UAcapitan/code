from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls.base import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import *
from .forms import *
from .utils import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.core.mail import send_mail

menu = ['Main page', 'Articles', 'About']

# class ArticleMain(ListView):
#     model = Article
#     template_name = 'appmain/index.html'
#     context_object_name = 'articles'

#     def get_context_data(self, *, object_list = None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['menu'] = menu
#         context['title'] = 'Main page'
#         return context

#     def get_queryset(self):
#         return Article.objects.filter(is_published=True)

@cache_page(60)
def index(request):
    articles = Article.objects.all()
    context = {
        'title':'Main page', 
        'menu':menu,
        'articles':articles
    }
    return render(request, 'appmain/index.html', context)

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

@login_required
def articles(request):
    contact_list = cache.get('cats')
    if not contact_list:
        contact_list = Article.objects.all()
        cache.set('cats', contact_list, 60)
    paginator = Paginator(contact_list, 3)
    # articles = Article.objects.all()
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        # 'articles':articles,
        'page_obj': page_obj
    }
    return render(request, 'appmain/articles.html', context)

class CategoryPage(LoginRequiredMixin, DataMixin, ListView):
    model = Category
    template_name = 'appmain/category.html'
    context_object_name = 'cats'
    login_url = reverse_lazy('main')
    raise_exception = False

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Category'
        c_def = self.get_user_context()
        return context | c_def

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

def orm_commands(request):
    return render(request, 'appmain/orm_commands.html')

def reg_view(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("main")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request, 'appmain/reg.html', {"register_form":form})

def login_view(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
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
	form = AuthenticationForm()
	return render(request=request, template_name="appmain/login.html", context={"login_form":form})

def logout_view(request):
    logout(request)
    messages.info(request, "You have successfully logged out.") 
    return redirect("main")

def send_emails(request):
    send_mail(
        'Subject here',
        'Here is the message.',
        'ua.capitan@testtrainingsite.com',
        ['ua.capitan@gmail.com'],
        fail_silently=False,
    )
    return redirect('main')

def form_email(request):
    if request.method == "POST":
        form = AddEmail(request.POST)
        if form.is_valid():
            form.save()
            return redirect("main")
    form = AddEmail()
    return render(request, 'appmain/form_email.html', {'form':form})

def pageNotFound(request, exception):
    return HttpResponseNotFound(f'<h1>Page not found</h1>')