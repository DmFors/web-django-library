from django import forms

BOOK_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 6)]


class CartAddBookForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=BOOK_QUANTITY_CHOICES, coerce=int)
    set_quantity = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
