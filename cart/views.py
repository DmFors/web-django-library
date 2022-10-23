from django.shortcuts import redirect, get_object_or_404, render
from django.views.decorators.http import require_POST
from library.models import Book
from .cart import Cart
from .forms import CartAddBookForm


@require_POST
def cart_add(request, book_id):
    cart = Cart(request)
    book = get_object_or_404(Book, id=book_id)
    form = CartAddBookForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(book=book, quantity=cd['quantity'], set_quantity=cd['set_quantity'])
        return redirect('cart_detail')


def cart_remove(request, book_id):
    cart = Cart(request)
    book = get_object_or_404(Book, id=book_id)
    cart.remove(book)
    return redirect('cart_detail')


def cart_detail(request):
    cart = Cart(request)
    context = {'cart': cart}
    return render(request, 'cart/cart_detail.html', context)
