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
            return redirect('main_app:index')
        else:
            error = 'Error, form not valid'

    form = Task_form()
    context = {
        'form':form,
        'error':error
    }
    return render(request, 'main/create.html', context)

def delete(request, index_task):
    try:
        Task.objects.get(id=index_task).delete()
        context = {
            'index_task':index_task,
            'error':''
        }
    except:
        context = {
            'index_task':'',
            'error':'Error 404. Task not found'
        }

    return render(request, 'main/delete.html', context)