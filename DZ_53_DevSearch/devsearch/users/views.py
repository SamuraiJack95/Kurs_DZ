from django.shortcuts import render, redirect
from .models import Profile, User
from django.contrib.auth import logout, login, authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def login_user(request):
    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username= request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except ObjectDoesNotExist:
            messages.error(request, 'User with this username does not exists')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, 'Username or password is incorrect')

    return render(request, 'users/login_register.html')

def logout_user(request):
    logout(request)
    messages.error(request, 'User was logged out')
    return redirect('login')

def profiles(request):
    prof = Profile.objects.all()
    context = {'profiles': prof}
    return render(request, 'users/index.html', context)

def user_profile(request, pk):
    prof = Profile.objects.get(id=pk)
    top_skills = prof.skills_set.exclude(description__exact='')
    other_skills = prof.skills_set.filter(description__exact='')
    context = {'profile': prof, 'top_skills': top_skills, 'other_skills': other_skills}
    return render(request, 'users/profile.html', context)

def register_user(request):
    page = 'register'
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'User account was created!')
    context = {'page': page, 'form': form}
    return render(request, 'users/login_register.html', context)