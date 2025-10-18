from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Example App!")

def about(request):
    return render(request, 'example_app/about.html')