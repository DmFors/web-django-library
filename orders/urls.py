from django.urls import path
from . import views
from .views import OrderListView

urlpatterns = [
    path('create', views.order_create, name='order_create'),
    path('',  OrderListView.as_view(), name='order_list'),
]