from django import forms
from . import models

class ProfileForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        exclude = ['user']
        widgets = {
            'gender':forms.RadioSelect(),
            'age':forms.TextInput()
        }

        