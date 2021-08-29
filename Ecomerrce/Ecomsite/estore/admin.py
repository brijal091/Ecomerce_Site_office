from django.contrib import admin
from .models import *
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(razorpay_Payment)
admin.site.register(Coupon_code)