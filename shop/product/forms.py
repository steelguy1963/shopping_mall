from django import forms
from product import models


class ProductForm(forms.ModelForm):
    class Meta:
        model = models.Product
        exclude = ['Id']
        widgets = {
            'Name': forms.TextInput(),
            'Thumbnail': forms.FileInput(),
            'Price': forms.TextInput(),
            'Stock': forms.TextInput(),
            'Country': forms.RadioSelect(),
            'Abstract': forms.TextInput()
        }

