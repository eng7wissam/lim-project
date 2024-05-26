from django.shortcuts import render
from .models import Product

# Create your views here.

def product(request):
    return render(request, 'products/product.html', {'pro':Product.objects.get(id=3)})

def products(request):
    pro = Product.objects.all()#all to filter
    #x = {'pro':str(pro.count())}
    #x = {'pro':pro.order_by('price')}#pro.filter(price=300)
    #x = {'pro':pro.exclude(price=300)} #except
    #x = {'pro':pro.filter(price__exact=300)}
    #x = {'pro':pro.filter(name__contains='l')}
    #x = {'pro':pro.filter(price__in=[300, 500, 600])}
    #x = {'pro':pro.filter(price__range=[10,600])}
    x = {'pro':pro}
    return render(request, 'products/products.html', x) #'pro':Product.objects.all()  'pro':Product.objects.get{id=1}  {'name':'ali'}
