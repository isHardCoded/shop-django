from django.shortcuts import render

from cart.models import CartItem
from orders.models import Order, OrderItem


def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)

    if request.method == "POST":
        order = Order.objects.create(user=request.user)

        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity
            )

        cart_items.delete()
        return render(request, "orders/order_success.html", {
            "order": order,
        })

    # добавить оплату

    total_price = sum(item.get_total_price() for item in cart_items)
    return render(request, "orders/checkout.html", {
        "cart_items": cart_items,
        "total_price": total_price
    })

