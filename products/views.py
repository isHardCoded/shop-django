from django.shortcuts import render
from .models import *

def home(request):
    return render(request, 'products/home.html', context={
        "products": Product.objects.all(),
        "categories": ProductCategory.objects.all()
    })

def products_by_category(request, category_id):
    category = ProductCategory.objects.get(id=category_id)
    products = Product.objects.filter(category=category)

    return render(request, 'products/home.html', context={
        "products": products,
        "categories": ProductCategory.objects.all(),
        "current_category": category_id,
    })