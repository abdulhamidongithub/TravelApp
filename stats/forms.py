from django import forms
from .models import *

class JourneyForm(forms.ModelForm):
    class Meta:
        model = Journey
        fields = '__all__'

