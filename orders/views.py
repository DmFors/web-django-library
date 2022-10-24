from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from cart.cart import Cart
from .forms import OrderCreateForm
from .models import Order, OrderItem
from main.models import User


def order_create(request):
    if 'username' not in request.session:
        print('not auth')
        return redirect('login')
    else:
        print('USERNAME: ', request.session['username'])
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        print('here')
        if form.is_valid():
            order = form.save()
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

    def get_context_data(self, *, object_list=None, **kwargs):
        object_list = Order.objects\
            .filter(username_id=get_object_or_404(User, username=self.request.session['username']).id).order_by('id')
        return super().get_context_data(object_list=object_list)
