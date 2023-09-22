from django.shortcuts import render
from .search import lookup
from productsApp.models import Product
# Create your views here.

def search_view(request):
    query_params = request.GET
    q = query_params.get('q')

    context = {}

    if q is not None:
        results = lookup(q)
        context['results'] = results
        context['query'] = q
    return render(request, 'search.html', context)

def display_product_details(request, pk=None): 
    if pk: 
        product = Product.objects.get(pk=pk)
    else: 
        product = "" 
    return render(request, 'product.html', {"product": product}) 