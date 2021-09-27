from django.forms import ModelForm
from .models import Product
from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)


class ProductCreationForm(ModelForm):
    class Meta:
        model = Product
        fields = ['model', 'description', 'price', 'availability', 'categories', 'manufacturer']
