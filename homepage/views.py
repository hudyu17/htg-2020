from django.shortcuts import render
from .models import Product

# Create your views here.
def index(request):

    products = Product.objects.all()

    product_list = []
    
    for product in products:
        product_dict = {
            'name': product.name, 
            'store': product.store,
            'location': product.location
        }
        product_list.append(product_dict)

    context = {'product_list': product_list}

    return render(request, 'homepage/homepage.html', context)