from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from . import forms
from django.contrib.auth.forms import AuthenticationForm


def main(request):
    return render(request, 'appmain/main.html', )

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
    return render(request, "appmain/login.html", {"login_form":form})

def logout_view(request):
    logout(request)
    messages.info(request, "You have successfully logged out.") 
    return redirect("main")

def profile(request):
    return render(request, 'appmain/profile.html')

def article(request):
    return render(request, 'appmain/article.html')

def favourite(request):
    return render(request, 'appmain/favourite.html')

def rate(request):
    return render(request, 'appmain/rate.html')

def list_of_articles(request):
    return render(request, 'appmain/list_of_articles.html')

def add_article(request):
    return render(request, 'appmain/add_article.html')

def recommendation(request):
    return render(request, 'appmain/recommendation.html')

def set_recommendation(request):
    if request.method == 'POST':
        return redirect('recommendation')
    return render(request, 'appmain/set_recommendation.html')

def admin_page(request):
    if request.user.is_staff:
        return render(request, 'appmain/admin_page.html')