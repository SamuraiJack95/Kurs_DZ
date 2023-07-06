from .models import Video
from pathlib import  Path
from django.shortcuts import get_object_or_404

# request, video_pk: int

# def open_file(file) -> tuple:
#
#     path = Path(file.path)
#
#     # file = path.open('rb')
#     return path.open('rb')