from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'author', 'cost', 'publish_year']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название книги',
            }),
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Автор',
            }),
            'cost': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена',
            }),
            'publish_year': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Год издания',
            }),
        }
        error_messages = {
            'publish_year': {
                'min_value': 'Пожалуйста, укажите год больше %(limit_value)s включительно :)',
                'max_value': 'Пожалуйста, укажите год меньше %(limit_value)s включительно :)',
            },
            'cost': {
                'min_value': 'Пожалуйста, введите цену больше %(limit_value)s включительно :)'
            }
        }
