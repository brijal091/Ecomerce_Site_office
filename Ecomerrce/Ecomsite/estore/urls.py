from django.urls import path
from . import views

urlpatterns = [
    path('', views.estore, name='estore'),
    path('cart/', views.cart, name='cart'),
    path('payment/', views.payment, name='payment'),
    path('updateItem/', views.updateItem, name='updateItem'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('paymentProceed/', views.paymentProceed, name='paymentProceed'),
    path('success/', views.success, name='success'),  
]
