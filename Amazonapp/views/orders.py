from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from Amazonapp.models.customer import Customer
from Amazonapp.models.product import Product
from Amazonapp.models.orders import Order

# # Create your views here.

class OrderView(View):
    def get(self , request):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        print('your order', orders)
        return render(request, 'orders.html', {'orders':orders})