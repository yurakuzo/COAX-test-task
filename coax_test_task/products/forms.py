from django import forms

from .models import Product


class OrderForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    product = forms.ModelChoiceField(queryset=Product.objects.all())