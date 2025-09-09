from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from cart.models import CartItem
from products.models import Product

@login_required(login_url='login')
def cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.get_total_price() for item in cart_items)
    return render(request, 'cart/cart.html', {'cart_items': cart_items, 'total_price': total_price})

@login_required(login_url='login')
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')

@login_required(login_url='login')
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    item.delete()
    return redirect('cart')

@login_required(login_url='login')
def change_quantity(request, item_id, action):
    item = get_object_or_404(CartItem, id=item_id)

    if action == 'increase':
        item.quantity += 1
        item.save()

    elif action == 'decrease':
       item.quantity -= 1

       if item.quantity <= 0:
           item.delete()
       else:
           item.save()

    return redirect('cart')

