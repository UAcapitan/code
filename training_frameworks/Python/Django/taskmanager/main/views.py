from django.shortcuts import render
from . import models


def index(request):
    tasks = models.Task.objects.all()
    context = {
        'tasks': tasks,
    }
    return render(request, 'main/index.html', context)

def page(request):
    return render(request, 'main/page.html')