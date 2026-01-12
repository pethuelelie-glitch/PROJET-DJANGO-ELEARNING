from os import name
from urllib import request
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import send_mail



# Create your views here.

def index(request):
    return render(request, 'index.html' )

def about(request):
    return render(request, 'about.html' )

def confirmation(request: HttpRequest):
    name = request.GET.get('name')
    email = request.GET.get('email')
    context = {'name': name, 'email': email}
    return render(request, 'confirmation.html', context)

def courses(request):
    return render(request, 'courses.html' )

def testimonial(request):
    return render(request, 'testimonial.html' )

def team(request):
    return render(request, 'team.html' )

def page_no_found(request):
    return render(request, '404.html' )

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        subject = f"message de {name}"
        body = f"""
        Nom = {name}
        Email = {email}
        subject = {subject}
        message = {message}
        """
        send_mail(subject,
        body,
        email,
        ['elp19129@gmail.com'])

        return redirect(
            reverse('confirmation') + f'?name={name}&email={email}'
    )


    return render(request, 'contact.html')