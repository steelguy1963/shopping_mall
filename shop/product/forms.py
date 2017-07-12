from django import forms
from product import models


class ProductForm(forms.ModelForm):
    class Meta:
        model = models.Product
        exclude = ['Id']
        widgets = {
            'Abstraction': forms.Textarea({'class':'form-active'})
        }

