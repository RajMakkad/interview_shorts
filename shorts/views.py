from django.shortcuts import render
from django.http import HttpResponse

shorts = [
    {
        'name': 'Raj Makkad',
        'time': '25May2023',
        'title': 'HackerEarth | Offcampus-Intern  | Interview Experience',
        'exp': '1 OA + 1 Tech + 1 Behaviour + 1 Hr'
    },
    {
        'name': 'Raj Makkad',
        'time': '26May2023',
        'title': 'Zscaler | Intern + FTE | Interview Experience',
        'exp': '1 OA + 3 Tech + 1 Hr'
    }
]

# In render content is sent as a dictionary, we can directly send a dictionary as a the third argument.
def home(request):
    data = {
        'shorts' : shorts,
        'title' : 'Home'
    }
    return render(request, 'shorts/home.html', data)