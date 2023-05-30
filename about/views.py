from django.shortcuts import render
from django.http import HttpResponse

def about(request):
    return render(request, 'about/about.html', {'title' : 'About'})

def contact(request):
    return render(request, 'about/contact.html', {'title' : 'Contact'})
