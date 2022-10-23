from django.conf import settings
from library.models import Book
from decimal import Decimal


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, book, quantity=1, set_quantity=False):
        """
        Добавляет книгу в корзину
        :param book: добавляемая книга
        :param quantity: количество
        :param set_quantity: количество добавляется к текущему (false) или
                            количество устанавливается в качестве текущего (true)
        :return:
        """
        book_id = str(book.id)
        if book_id not in self.cart:
            self.cart[book_id] = {'quantity': 0, 'cost': str(book.cost)}
        if set_quantity:
            self.cart[book_id]['quantity'] = quantity
        else:
            self.cart[book_id]['quantity'] += quantity
        self.save()

    def remove(self, book):
        """
        Удаляет книгу из корзины
        :param book: удаляемая книга
        :return:
        """
        book_id = str(book.id)
        if book_id in self.cart:
            del self.cart[book_id]
            self.save()

    def save(self):
        """Обновляет корзину в сессии"""
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def __iter__(self):
        # Добавление в корзину экземпляров книг из модели
        book_ids = self.cart.keys()
        cart_books = Book.objects.filter(id__in=book_ids)
        for book in cart_books:
            self.cart[str(book.id)]['book'] = book

        # Перебор элементов в корзине, добавление поля total_price
        for item in self.cart.values():
            item['cost'] = Decimal(item['cost'])
            item['total_price'] = item['cost'] * item['quantity']
            yield item

    def __len__(self):
        return len(self.cart)

    def get_total_quantity(self):
        """Общее количество книг в корзине"""
        self.get_total_price()
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        """Полная стоимость корзины"""
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        """Удаление корзины из сессии"""
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
