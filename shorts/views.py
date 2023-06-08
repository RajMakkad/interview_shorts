from django.shortcuts import render
from django.http import HttpResponse
from .models import Short
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required


def home(request):
    short = Short.objects.all()
    short = short.order_by('post_date').reverse()
    if not request.user.is_authenticated:
        messages.info(request, 'Login to see Wonders.')
    return render(request, 'shorts/home.html', {'shorts' : short, 'title' : 'Home'})


@login_required
def detailedShorts(request, short_id):
    try:
        short = Short.objects.get(id=short_id)
        return render(request, 'shorts/short.html', {'short' : short, 'title' : 'Short'})
    except:
        return render(request, 'shorts/i_exists.html', {'title' : 'Bitch!!'})