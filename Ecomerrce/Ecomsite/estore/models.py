from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, verbose_name='User')
    name = models.CharField(max_length=200, null=True, verbose_name='Name')
    email = models.CharField(max_length=200, null=True, verbose_name='Email')

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    date_order = models.DateField(auto_now_add=True, verbose_name='Ordered On')
    complete = models.BooleanField(default=False, null=True, blank=True)
    transaction_id = models.CharField(max_length=200, verbose_name='Transaction Id')

    def __str__(self):
        return str(self.customer.name)

    @property
    def shipping(self):
        shipping = False
        item_ordered = self.orderitem_set.all()
        for i in item_ordered:
            if i.product.digital == False:
                shipping == True
        return shipping

    @property
    def get_total_cart(self):
        item_ordered = self.orderitem_set.all()
        all_product_total = sum([item.get_total for item in item_ordered])
        return all_product_total

    @property
    def get_cart_items(self):
        item_ordered = self.orderitem_set.all()
        all_product_total = sum([item.quantity for item in item_ordered])
        return all_product_total


class Product(models.Model):
    name = models.CharField(max_length=200, null=True, verbose_name='Product Name')
    price = models.FloatField(verbose_name='Price')
    image = models.ImageField(null=True, verbose_name='Upload Product Image')

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, verbose_name='Quantity')
    check_status = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='Item Added On')

    def __str__(self):
        return self.product.name

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, verbose_name='Address')
    city = models.CharField(max_length=200, verbose_name='City')
    state = models.CharField(max_length=200, verbose_name='State')
    country = models.CharField(max_length=200, verbose_name='Country', null=True)
    Zip = models.CharField(max_length=200, verbose_name='Zip code', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='Address Added Date')

    def __str__(self):
        return self.customer.name

class razorpay_Payment(models.Model):
    name = models.CharField(max_length=100)
    Amount = models.IntegerField()
    order_id = models.CharField(max_length=100, blank=True)
    razorpay_payment_id = models.CharField(max_length=100, blank=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Coupon_code(models.Model):
    code = models.CharField(max_length=100)
    discount = models.IntegerField(null=True)
    status = models.BooleanField(default=False, verbose_name='Activate')
    def __str__(self):
        return self.code