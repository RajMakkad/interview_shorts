from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User, auth


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if username == '' or username == ' ':
            messages.info(request, 'Create username properly.')
            return redirect('register')
        if password1 == '' or password1 == ' ':
            messages.info(request, 'Create passwords properly.')
            return redirect('register')
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken.')
                return redirect('register')
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already taken.')
                return redirect('register')
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.save()
            messages.success(request, f'Account Created for {username}.!')
            return redirect('login')
        else:
            messages.info(request, 'Passwords are not matching.')
            return redirect('register')
    else:
        return render(request, 'users/register.html', {'title': 'Register'})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, f'{username}  logged in.')
            return redirect('home')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html', {'title': 'Login'})
    
def logout(request):
    auth.logout(request)
    messages.info(request, 'logged out.')
    return redirect('home')

