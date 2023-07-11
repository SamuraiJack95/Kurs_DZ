from django.forms import ModelForm
from .models import Skills

class SkillsForm(ModelForm):
    class Meta:
        model = Skills
        fields = ['title', 'description', 'url', 'image']