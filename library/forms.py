from django.forms import ModelForm, TextInput, NumberInput
from .models import Book


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'author', 'cost', 'publish_year']
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название книги',
            }),
            'author': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Автор',
            }),
            'cost': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена',
            }),
            'publish_year': NumberInput(attrs={
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
