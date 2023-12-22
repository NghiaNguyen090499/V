# forms.py
from django import forms
from django.forms import modelformset_factory
from .models import Achievement

class AchievementForm(forms.ModelForm):
    class Meta:
        model = Achievement
        fields = ['completed']
        widgets = {
            'completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

AchievementFormSet = modelformset_factory(Achievement, form=AchievementForm, extra=0)
