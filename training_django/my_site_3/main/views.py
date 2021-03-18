from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello, world')

def about_us(request):
    return HttpResponse('About us')