from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('library/', include('library.urls'), namespace='library'),
    path('cart/', include('cart.urls'), namespace='cart'),
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]
