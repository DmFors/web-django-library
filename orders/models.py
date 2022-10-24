from django.core.validators import MinValueValidator
from django.db import models
from main.models import User
from library.models import Book


class Order(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders', null=True)
    first_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f'Order {self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    book = models.ForeignKey(Book, on_delete=models.PROTECT, related_name='order_items')
    cost = models.FloatField(validators=[MinValueValidator(0)])
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.cost * self.quantity
