from django.contrib import admin

from .models import Taste, Base, Product, Review, Order, OrderItem

admin.site.register(Taste)
admin.site.register(Base)
admin.site.register(Product)

admin.site.register(Order)
admin.site.register(OrderItem)

