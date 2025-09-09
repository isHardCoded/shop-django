from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('categories/<int:category_id>/', products_by_category, name='products_by_category'),
]