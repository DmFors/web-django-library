from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('library/', include('library.urls')),
    path('cart/', include('cart.urls')),
    path('orders/', include('orders.urls')),
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]
