from django.shortcuts import render
from .models import Skills
from .models import Video
from .models import Works
# Create your views here.

def index(request):
    projects = Skills.objects.all()
    return render(request, 'skills/index.html', {'projects': projects})

def video_get(request):
    vid = Video.objects.all()
    wor = Works.objects.all()
    return render(request, 'skills/works.html', {'vid': vid}, {'wor': wor})