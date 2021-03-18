from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import Task_form


def index(request):
    tasks = Task.objects.all()
    return render(request, 'main/index.html', {'title':'Main page', 'tasks':tasks})

def about(request):
    return render(request, 'main/about.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = Task_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = 'Error, form not valid'

    form = Task_form()
    context = {
        'form':form,
        'error':error
    }
    return render(request, 'main/create.html', context)