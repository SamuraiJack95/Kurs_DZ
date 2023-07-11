from django.contrib import admin
from .models import Skills
from .models import Video
from .models import Works

# Register your models here.

class SkillsAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(Skills)
admin.site.register(Video)
admin.site.register(Works)

