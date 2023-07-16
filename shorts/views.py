from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Short
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required


data = {
    'title': '',
    'ctc': '',
    'experience': '',
    'offer': '',
    'difficulty': ''
}

def home(request):
    short = Short.objects.all()
    short = short.order_by('post_date').reverse()
    if not request.user.is_authenticated:
        messages.info(request, 'Login to see Wonders.')
    return render(request, 'shorts/home.html', {'shorts':short, 'title':'Home', 'experience': False})


@login_required
def detailedShorts(request, short_id):
    try:
        short = Short.objects.get(id=short_id)
        return render(request, 'shorts/short.html', {'short' : short, 'title' : 'Short'})
    except:
        message = 'Bitch please, Go back & Create your own shorts!!!'
        return render(request, 'shorts/i_exists.html', {'title' : 'Bitch!!', 'message':message})
    
@login_required
def my_shorts(request):
    user = request.user
    short = Short.objects.all().filter(author=user)
    short = short.order_by('post_date').reverse()
    message = ''
    if len(short) == 0:
        message = 'You have not written any shorts yet!!'
    return render(request, 'shorts/home.html', {'shorts':short, 'title':user.username, 'message':message, 'experience': True})

@login_required
def create_shorts(request):
    if request.method == 'POST':
        response = request.POST
        author = request.user
        title = response['title']
        ctc = response['ctc']
        difficulty = response['difficulty']
        experience = response['experience']
        offer = response['offer']
        short = Short(author=author, title=title, ctc=ctc, difficulty=difficulty, experience=experience, offer=offer)
        short.save()
        messages.success(request, f'A Short created with the Title, {title}.!')
        return redirect('shorts-home')
    else:
        return render(request, 'shorts/create.html', {'title':'Experience', 'data':data})

@login_required
def delete_shorts(request, short_id):
    try:
        user = request.user
        short = Short.objects.get(id=short_id)
        if user != short.author:
            raise Exception('Go away!')
        title = short.title
        short.delete()
        messages.success(request, f'Successfully deleted the short with the Title, {title}')
        return render(request, 'shorts/short.html', {'short' : short, 'title' : 'Short'})
    except:
        message = 'Bitch please, Go back & Cause no more shorts to delete!!!'
        return render(request, 'shorts/i_exists.html', {'title' : 'Bitch!!', 'message':message})
    

@login_required
def update_shorts(request, short_id):
    try:
        user = request.user
        short = Short.objects.get(id=short_id)
        if user != short.author:  raise Exception('Go away!')
        if request.method == 'POST':
            response = request.POST
            short.title = response['title']
            short.ctc = response['ctc']
            short.difficulty = response['difficulty']
            short.experience = response['experience']
            short.offer = response['offer']
            short.save()
            messages.success(request, f'Successfully updated the short with the Title, {short.title}')
            return redirect('detailedShorts', short_id=short_id)
        else:
            data['title'] = short.title
            data['ctc'] = short.ctc
            data['experience'] = short.experience
            data['offer'] = short.offer
            data['difficulty'] = short.difficulty
            return render(request, 'shorts/create.html', {'data' : data, 'title' : 'Short'})
    except:
        message = 'Bitch please, Go back & Cause no more shorts to update!!!'
        return render(request, 'shorts/i_exists.html', {'title' : 'Bitch!!', 'message':message})