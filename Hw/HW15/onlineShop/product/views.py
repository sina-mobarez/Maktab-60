from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from datetime import datetime

# Create your views here.

def get_time_now(request):
    return HttpResponse(f'Now time is : {datetime.now()}')


def show_product_detail(request, index):
    product = Product.objects.filter(id=index)
    return HttpResponse(f'<html><body><h1>{product[0].name}</h1></body></html>')


def show_product_template(request):
    product = Product.objects.all()
    return render(request, 'product.html', {'product': product})

