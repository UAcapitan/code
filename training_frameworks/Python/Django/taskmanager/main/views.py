from django.shortcuts import render, redirect
from . import models
from . import forms


def index(request):
    tasks = models.Task.objects.all()
    context = {
        'tasks': tasks,
    }
    return render(request, 'main/index.html', context)

def page(request):
    return render(request, 'main/page.html')

def create(request):
    form = forms.TaskForm()
    context = {
        'form': form,
    }
    if request.method == "POST":
        form = forms.TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('main')
    else:
        return render(request, 'main/create.html', context)