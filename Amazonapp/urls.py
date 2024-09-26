from django.contrib import admin
from django.urls import path,include 
from .views import home 
from .views import login
from .views import signup
from .views import cart
from Amazonapp.views.login import logout
from .views import checkout
from .views import orders

urlpatterns = [
    path('', home.index.as_view() ,name="homepage"),
    path('signup', signup.signup.as_view(), name="signuppage"),
    path('login', login.login.as_view(), name='loginpage'),
    path('logout', logout, name='logoutpage'),
    path('cart', cart.Cart.as_view(), name='cartpage'),
    path('check-out', checkout.checkOut.as_view(), name='checkout'),
    path('orders', orders.OrderView.as_view(), name='orders')
]
