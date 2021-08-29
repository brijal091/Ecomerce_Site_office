import json
# from os import PRIO_PGRP, chmod
from django import contrib
import django
from django.core.checks import messages
from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
import razorpay
from .models import razorpay_Payment
from django.http import HttpResponse
import time

# Create your views here.
def estore(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_total_cart': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']

    Products = Product.objects.all()
    context = {'Products': Products, 'cartItems': cartItems}
    return render(request, 'estore/estore.html', context)

@login_required(login_url='login')
def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'estore/cart.html', context)


def payment(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items

    else:
        items = []
        order = {'get_total_cart': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']
    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'estore/payment.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(
        customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(
        order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse('Item added', safe=False)


def login(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        password = request.POST['pass']

        user = auth.authenticate(username=user_name, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'User Does not Exist')
            return redirect('/login/')
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_name = request.POST['UserName']
        password = request.POST['password']
        email = request.POST['email']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=user_name).exists():
                messages.info(
                    request, 'User Already Exist. Please chose another one')
                return redirect('/register/')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Exist.')
                return redirect('/register/')
            else:
                user = User.objects.create_user(username=user_name, first_name=first_name, last_name=last_name,
                                                password=password, email=email)
                user.save();
                customer_id = User.objects.get(id=user.id)
                create_customer = Customer.objects.create(
                    name=user_name, email=email, user_id=customer_id.id)
                create_customer.save();
                return redirect('/login/')
        else:
            messages.info(request, "Please Enter Same Password")
            return redirect('/register/')
    else:
        return render(request, 'registration.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def paymentProceed(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        cartTotal = order.get_total_cart
    if request.method == 'POST':
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        country = request.POST['country']
        zip = request.POST['zipcode']
        cupon_code = request.POST['cupon_code']
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
    if request.method == 'POST':
        client = razorpay.Client(
            auth=("rzp_test_kwHK8oF2E8PSYQ", "LuVJHBXPpeJaKsWLV22k6ngR"))
        amount_Rupee = int(order.get_total_cart)
        if cupon_code == "":
            final_amount = amount_Rupee
            discount_amt = 0
        else:
            coupon = Coupon_code.objects.all()
            coupon = str(coupon)
            if cupon_code in coupon:
                cupon_get = Coupon_code.objects.get(code = cupon_code)
                if cupon_get.status == True:
                    discount = cupon_get.discount
                    discount_amount = ((discount * amount_Rupee)/100)
                    final_amount = amount_Rupee - discount_amount
                    discount_amt = discount
                else:
                    final_amount = amount_Rupee
                    messages.info(request,"Sorry Cupon is not Active at this movement")
                    return redirect('/payment/')
            else:
                final_amount = amount_Rupee
                messages.info(request,"Invalid Coupn Code")
                return redirect('/payment/')
        amount = int(final_amount)*100
        # print(discount_amt)
        order_currency = 'INR'
        response_Payment = client.order.create(
            dict(amount= amount, currency = order_currency, payment_capture=1))
        order_id = response_Payment['id']
        order_status = response_Payment['status']
        user1 = request.POST['Name']
        customer_Email = request.POST['Email']

        if order_status == 'created':
            payment_info = razorpay_Payment.objects.create(name=user1, Amount=amount/100, order_id=order_id)
            payment_info.save();
        shipping_address=ShippingAddress.objects.create(
            address=address, city=city, state=state, country=country, Zip=zip, customer_id=customer.id, order_id=order.id)
        shipping_address.save();

    return render(request, 'paysucess.html', {"discount_amt": discount_amt,"response_Payment": response_Payment, "Name": user1, "Email": customer_Email, 'order_id': order_id, 'items':items, 'cartItems':cartItems, 'amount':final_amount})

def success(request):
    response=request.POST
    client = razorpay.Client(auth = ('rzp_test_kwHK8oF2E8PSYQ', 'LuVJHBXPpeJaKsWLV22k6ngR'))
    params_dict = {
        'razorpay_order_id': response['razorpay_order_id'],
        'razorpay_payment_id': response['razorpay_payment_id'],
        'razorpay_signature': response['razorpay_signature']
    }
    try:
        client.utility.verify_payment_signature(params_dict)
        razorpay_payment__Info = razorpay_Payment.objects.get(order_id = response['razorpay_order_id'])
        razorpay_payment__Info.razorpay_payment_id = response['razorpay_payment_id']
        razorpay_payment__Info.paid = True
        razorpay_payment__Info.save();
    except:
        razorpay_payment__Info.paid = False
        return render(request, 'success.html',{'status':False})
    else:
        
        Order_items = OrderItem.objects.all()
        for item in Order_items:
            item.check_status = True
            item.save();
        customer = request.user.customer
        order = Order.objects.get(customer=customer, complete=False)
        order.complete = True
        order.save();
        return render(request, 'success.html',{'status':True})