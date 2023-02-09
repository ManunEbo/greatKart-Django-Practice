from django.shortcuts import render
from store.models import product

def home(request):
    # retrieving all the products for display on the home page
    products = product.objects.all().filter(is_available=True)

    context = {
        'products': products,
    }

    return render(request,'home.html', context)