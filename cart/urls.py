from django.urls import path
from .views import *

urlpatterns = [
    path('', cart, name='cart'),
    path('add/<int:product_id>/', add_to_cart, name='add_to_cart'),
]

# http://127.0.0.1:8000/cart/ - открыть корзину
# http://127.0.0.1:8000/cart/add/id - добавлять товар