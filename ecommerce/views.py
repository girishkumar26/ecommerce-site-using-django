from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'shop.html')


def product(request):
    return render(request, 'product-single.html')
