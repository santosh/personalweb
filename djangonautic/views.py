from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("<h1>You are looking at home page.</h1>")
    return render(request, 'homepage.html')

def about(request):
    # return HttpResponse("You are looking at about page.")
    return render(request, 'about.html')
