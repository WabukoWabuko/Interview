from django import forms
from .models import Product
# This file defines a ModelForm for the Product model.
# form.py in this case is used to create and update Product instances.
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image']