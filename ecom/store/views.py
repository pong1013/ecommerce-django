from django.shortcuts import render
from .models import Product

def home(request):
    products = Product.objects.all()
    return render(request, 'navbar/home.html', {'products':products})

def about(request):
    return render(request, 'navbar/about.html',{})