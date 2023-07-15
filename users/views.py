from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from .models import Profile


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
            return redirect('shorts-home')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'users/login.html', {'title': 'Login'})
    
def logout(request):
    auth.logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('login')

@login_required
def profile(request):
    if request.method == 'POST':
        old_username = request.user.username
        old_email = request.user.email
        old_branch = request.user.profile.branch
        username = request.POST['username']
        email = request.POST['email']
        branch = request.POST['branch']
        if username == '' and email == '' and branch == '':
            messages.info(request, f'{old_username}, you left all the fields empty!')
        if username == '' or username == ' ':
            username = old_username
        if email == '' or email == ' ':
            email = old_email
        if branch == '' or branch == ' ':
            branch = old_branch
        if old_username != username:  
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken.')
                return redirect('profile')
        if old_email != email:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already taken.')
                return redirect('profile')
        User.objects.filter(username=old_username).update(username=username, email=email)
        Profile.objects.filter(user=request.user).update(branch=branch)
        return redirect('profile')
    else:
        username = request.user.username
        return render(request, 'users/profile.html', {'title' : username})
