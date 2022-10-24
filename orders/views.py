from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from cart.cart import Cart
from .forms import OrderCreateForm
from .models import Order, OrderItem
from main.models import User


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        print('here')
        if form.is_valid():
            order = form.save()
            if 'username' in request.session:
                order.username = get_object_or_404(User, username=request.session['username'])
            order.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    book=item['book'],
                    cost=item['cost'],
                    quantity=item['quantity'],
                )
            cart.clear()
            context = {'order': order}
            return render(request, 'orders/order_created.html', context)
    else:
        form = OrderCreateForm
    context = {'cart': cart, 'form': form}
    return render(request, 'orders/order_create.html', context)


class OrderListView(ListView):
    model = Order
    paginate_by = 100
