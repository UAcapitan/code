from django.shortcuts import render
from django.http import HttpResponse
from .models import Task


def index(request):
    tasks = Task.objects.all()
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')