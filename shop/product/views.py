# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from product.models import Product
from product.forms import ProductForm

# Create your views here.

def listProduct(request):
	pList = Product.objects.all()
	return render(request, 'list.html', {'pList':pList})

def showProduct(request, product_id):
	pShow = get_object_or_404(Product, pk=product_id)
	return render(request, 'product.html', {'pShow':pShow})

def listProduct_edit(request):
	pList = Product.objects.all()
	return render(request, 'list_edit.html', {'pList':pList})


def editProduct(request, product_id):
    product_info = None
    try:
		product_info = get_object_or_404(Product, pk=product_id)
    except:
		product_info = None
    form = ProductForm(request.POST or None, instance=product_info)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/list_edit/')


    return render(request, 'product_edit.html', {'form':form})
