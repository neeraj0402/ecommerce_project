from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order

class AdminProduct(admin.ModelAdmin):
    list_display = [
        'name',
        'price',
        'category_id',
        'description',
        'image',
    ]

class AdminCategory(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
    ]

class AdminCustomer(admin.ModelAdmin):
    list_display=[
        'first_name',
        'last_name',
        'email',
        'phone',
        'password',
    ]

class AdminOrder(admin.ModelAdmin):
    list_display=[
        'product',
        'customer',
        'quantity',
        'price',
        # 'address',
        # 'phone',
        'date',
        # 'status'
    ]

# class AdminOrder(admin.ModelAdmin):
#     list_display=[
#         'product',
#         'customer',
#         'quantity',
#         'price',
#         'address',
#         # 'phone',
#         'date'
#     ]

admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Customer, AdminCustomer)
# admin.site.register(Order)
admin.site.register(Order, AdminOrder)