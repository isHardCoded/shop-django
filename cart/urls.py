from django.urls import path
from .views import *

urlpatterns = [
    path('', cart, name='cart'),
    path('add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    path('<str:action>/change/quantity/<int:item_id>/', change_quantity, name='change_quantity'),
]

# http://127.0.0.1:8000/action/change/quantity/id - изменить количество
# http://127.0.0.1:8000/cart/ - открыть корзину
# http://127.0.0.1:8000/cart/add/id - добавлять товар
# http://127.0.0.1:8000/cart/remove/id - удалить товар