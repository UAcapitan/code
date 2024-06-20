
from django.shortcuts import render
from django.http import HttpResponse
from . import models

def index(request):
    return HttpResponse("<h1>Working</h1>")

def main(request):
    return render(request, "main/main.html")