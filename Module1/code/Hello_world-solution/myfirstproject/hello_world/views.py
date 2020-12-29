from django.shortcuts import render

# [TODO]: Add code below to create view
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world!")