from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse('Hello')
    # return render(request, 'main_app/index.html', [])
