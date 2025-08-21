from django.shortcuts import render
from .models import *

def home(request):
    return render(request, 'products/home.html', context={
        "products": Product.objects.all()
    })

