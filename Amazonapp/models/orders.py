from django.db import models 
from .product import Product
from .customer import Customer
import datetime

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField(default=0)
    # address = models.CharField(max_length=50, default=0, blank=True)
    # phone = models.IntegerField(blank=True, null=True, default=None)
    date = models.DateField( default=datetime.datetime.today)
    status = models.BooleanField(default=False)


    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer = customer_id)
    