from django.shortcuts import render

def home(request):
    context = {
        'name':'Ivan'
    }
    return render(request, 'main/home.html', context)