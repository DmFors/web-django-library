from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'address', 'city']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваше имя'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваш адрес'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваш город'}),
        }
