from django.forms import ModelForm
from .models import Product
from django import forms


class Product_Form(ModelForm):

    class Meta:
        model = Product
        fields = "__all__"

        widgets = {
            'product_name': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'product_code': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'price': forms.NumberInput(
                attrs={'class': 'form-control'}
            ),
            'gst': forms.NumberInput(
                attrs={'class': 'form-control'}
            ),
            'picture':forms.FileInput(attrs={'class':'form-control'}),
        }