from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .forms import SkillsForm
from django.utils import timezone
from .models import Skills
from .models import Works


def index(request):
    projects = Skills.objects.filter(user=request.user)
    return render(request, 'skills/index.html', {'projects': projects})
@login_required
def detail(request, work_id):
    work = get_object_or_404(Works, pk=work_id)
    return render(request, 'skills/detail.html', {'work': work})
@login_required
def video_get(request):
    wor = Works.objects.all()
    # file = open_file(wor[0])
    # vid = Video.objects.all()

    return render(request, 'skills/works.html', {'wor': wor})

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'skills/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('index')
            except IntegrityError:
                return render(request, 'skills/singupuser.html', {'form': UserCreationForm(), 'error': 'имя пользователя уже существует! Попробуйте другое'})
        else:
            print('Пароли не совпадают!')


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'skills/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'skills/loginuser.html', {'form': AuthenticationForm(), 'error': 'Неверные данные для входа!'})
        else:
            login(request, user)
            return redirect('index')

@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


@login_required
def currentskills(request):
    skills = Skills.objects.filter(user=request.user)
    return render(request, 'skills/index.html', {'skills': skills})


@login_required
def createskills(request):
    if request.method == 'GET':
        return render(request, 'skills/createskills.html', {'form': SkillsForm()})
    else:
        try:
            form = SkillsForm(request.POST)
            new_skills = form.save(commit=False)
            new_skills.user = request.user
            new_skills.save()
            return redirect('index')
        except ValueError:
            return render(request, 'skills/createskills.html', {'form': SkillsForm(), 'error': 'Переданы неверные данные, попробуйте снова'})


@login_required
def viewskills(request, skills_pk):
    skills = get_object_or_404(Skills, pk=skills_pk)
    if request.method == 'GET':
        form = SkillsForm(instance=skills)
        return render(request, 'skills/viewskills.html', {'skills': skills, 'form': form})
    else:
        try:
            form = SkillsForm(request.POST, instance=skills)
            form.save()
            return redirect('index')
        except ValueError:
            return render(request, 'skills/viewskills.html', {'skills': skills, 'form': form, 'error': 'неверные данные'})


@login_required
def deleteskills(request, skills_pk):
    skills = get_object_or_404(Skills, pk=skills_pk, user=request.user)
    if request.method == 'POST':
        skills.date_completed = timezone.now()
        skills.delete()
        return redirect('index')


def home(request):
    return render(request, 'skills/home.html')