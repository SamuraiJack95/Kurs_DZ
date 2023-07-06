from django.shortcuts import render, get_object_or_404
from .models import Skills
from .models import Video
from .models import Works
# from .servic import open_file
# Create your views here.

def index(request):
    projects = Skills.objects.all()
    return render(request, 'skills/index.html', {'projects': projects})

def detail(request, work_id):
    work = get_object_or_404(Works, pk=work_id)
    return render(request, 'skills/detail.html', {'work': work})

def video_get(request):
    wor = Works.objects.all()
    # file = open_file(wor[0])
    # vid = Video.objects.all()

    return render(request, 'skills/works.html', {'wor': wor})