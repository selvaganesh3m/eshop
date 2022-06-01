from django.shortcuts import render
from django.views import View
from .models import Product


# Create your views here.

class ProductView(View):
    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        return render(request, 'products/products.html', {'products': products})
