from django.shortcuts import render
import random

# Create your views here.


def home(request):
    length = list(range(8, 16))
    return render(request, 'generator/home.html', {'lst': length})

def password(request):
    chars = [chr(i) for i in range(97, 123)]

    if request.GET.get('uppercase'):
        chars.extend([chr(i) for i in range(65, 91)])

    if request.GET.get('numbers'):
        chars.extend([chr(i) for i in range(48, 58)])

    if request.GET.get('special'):
        chars.extend([chr(i) for i in range(33, 48)])

    length = int(request.GET.get('length'))
    psw = ''.join(random.choices(chars, k=length))
    return render(request, 'generator/password.html', {'password': psw})

def about(request):
    return render(request, 'generator/about.html')