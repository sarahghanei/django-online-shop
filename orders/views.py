from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem
from cart.cart import Cart
from suds.client import Client


@login_required
def detail(request, order_id):
	order = get_object_or_404(Order, id=order_id)
	return render(request, 'orders/order.html', {'order':order})

@login_required
def order_create(request):
	cart = Cart(request)
	order = Order.objects.create(user=request.user)
	for item in cart:
		OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
		cart.clear()
	return redirect('orders:detail', order.id)


MERCHANT = 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'
client = Client('https://www.zarinpal.com/pg/services/WebGate/wsdl')
amount = 1000
description = "پرداخت مونگارد"
email = 'email@example.com'
mobile = '09123456789'
CallbackURL = 'http://localhost:8000/orders/verify/'

def payment(request):
	pass

def verify(request):
	pass