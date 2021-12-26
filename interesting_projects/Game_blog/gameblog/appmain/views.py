from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from . import forms


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