from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404

def index(request):
    return HttpResponse('Hello, world')

def article(request, id):
    if (request.GET):
        print(request.GET)

    if (request.POST):
        print(request.POST)

    return HttpResponse(f'<h1>Page {str(id)}</h1>')

def year(request, year):
    if int(year) > 2021:
        raise Http404()
    if int(year) > 2000:
        return redirect('main')
    if int(year) > 1990:
        return redirect('main', permanent=True)
    return HttpResponse(f'<h1>Year {str(year)}</h1>')

def pageNotFound(request, exception):
    return HttpResponseNotFound(f'<h1>Page not found</h1>')
