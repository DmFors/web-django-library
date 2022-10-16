from django.urls import path
from . import views
from .views import RegisterUser, LoginUser

urlpatterns = [
    path('', views.redirect_library),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
]
