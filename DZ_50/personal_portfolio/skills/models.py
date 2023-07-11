from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



class Skills(models.Model):
    title = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=250, blank=True)
    image = models.ImageField(blank=True)
    url = models.URLField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('viewskills', kwargs={'skills_pk': self.pk})


class Works(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='works/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title

class Video(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='video/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title