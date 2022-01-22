from django import forms
from .models import Product

class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['quantity', 'price', 'name', 'image','description']
        
class ProductCreate(forms.ModelForm):
    class Meta:
        model = Product 
        fields = ['name','description','quantity', 'price','image']