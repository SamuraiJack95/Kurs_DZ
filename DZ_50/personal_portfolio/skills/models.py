from django.db import models

# Create your models here.
class Skills(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='skills/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title

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