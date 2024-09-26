from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from Amazonapp.models.customer import Customer
from django.views import View

# # Create your views here.

class signup(View):
    def get(self, request):
        return render(request, 'signin.html')
    
    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        # validation
        value = {
            'first_name' : first_name,
            'last_name' : last_name,
            'phone' : phone,
            'email' : email
        }
        error_message = None
        customer = Customer(first_name = first_name, last_name = last_name, phone = phone, email = email, password = password)
        error_message = self.validateCustomer(customer)
        # elif customer.isExists():
        #     error_message = 'phone no. already used'
        
        # saving
        if not error_message:
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
        
        else:
            data = {
                'error' :error_message,
                'values': value
            } # type: ignore
        return render(request, 'signin.html' , data)
    
    def validateCustomer(self, customer):
        error_message = None
        if (not customer.first_name):
            error_message = 'First Name Required !!'
        elif len(customer.first_name) < 4:
            error_message = 'First Name must be 4 char long or more'
        elif not customer.last_name:
            error_message = 'Last Name Required !!'
        elif len(customer.last_name) < 4:
            error_message = 'Last Name must be 4 char long or more'
        elif not customer.phone:
            error_message = 'Phone no. Required !!'
        elif len(customer.phone) < 10:
            error_message = 'Phone no. must be 10 char'
        elif not customer.password:
            error_message = 'password Required !!'
        elif len(customer.password) < 6:
            error_message = 'Password must be 6 char long or more'
        elif len(customer.email) < 5:
            error_message = 'Email Required !!'
        elif customer.isExists():
            error_message = 'Email Already Registered'

        return error_message






