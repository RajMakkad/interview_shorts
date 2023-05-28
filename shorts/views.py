from django.shortcuts import render
from django.http import HttpResponse
from .models import Short


def home(request):
    return render(request, 'shorts/home.html', {'shorts' : Short.objects.all(), 'title' : 'Home'})