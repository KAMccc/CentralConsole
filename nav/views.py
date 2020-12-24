from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def IndexView(request):
    return HttpResponse("Welcome to the navigator! _ kam")
