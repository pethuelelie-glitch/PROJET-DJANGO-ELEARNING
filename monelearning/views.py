from urllib import request
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html' )

def about(request):
    return render(request, 'about.html' )

def contact(request):
    return render(request, 'contact.html' )

def courses(request):
    return render(request, 'courses.html' )

def testimonial(request):
    return render(request, 'testimonial.html' )

def team(request):
    return render(request, 'team.html' )

def page_no_found(request):
    return render(request, '404.html' )