import decimal

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from basket.basket import Basket
from .forms import CheckoutForm
from .models import Order


# views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem
from .forms import CheckoutForm


"""
@login_required
def checkout(request):
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.total = calculate_total(request)  # Assume you have a function to calculate the total
            order.save()
            for item in get_cart_items(request):  # Assume you have a function to get cart items
                OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity)
            return redirect('orders:order_success', order_id=order.id)
    else:
        form = CheckoutForm()
    return render(request, 'orders/checkout.html', {'form': form})

def calculate_total(request):
    # Implement your total calculation logic here

    return 100  # Placeholder

def get_cart_items(request):
    # Implement your cart retrieval logic here
    return []  # Placeholder

"""

@login_required
def checkout(request):
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.total = calculate_total(request)
            order.save()
            for item in get_cart_items(request):
                OrderItem.objects.create(order=order, product=item['product'], quantity=item['qty'])
            return redirect('orders:order_success', order_id=order.id)
    else:
        form = CheckoutForm()
    return render(request, 'orders/checkout.html', {'form': form})

def calculate_total(request):
    cart_items = get_cart_items(request)
    shipping = 11.50
    total = sum(item['product'].price * item['qty'] for item in cart_items) + decimal.Decimal(shipping)
    return total

def get_cart_items(request):
    basket = Basket(request)
    return list(basket)


# views.py

@login_required
def order_success(request, order_id):
    order = Order.objects.get(id=order_id, user=request.user)
    return render(request, 'orders/order_success.html', {'order': order})

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders/order_history.html', {'orders': orders})

"""
@login_required
def checkout(request):
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            return redirect('orders:order_success')
    else:
        form = CheckoutForm()
    return render(request, 'orders/checkout.html', {'form': form})
from django.shortcuts import render

# Create your views here.
@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders/order_history.html', {'orders': orders})


@login_required
def order_success(request):
    return render(request, 'orders/order_success.html')
    
"""