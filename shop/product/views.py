# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from product.models import Product
from product.forms import ProductForm

import json

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


def createProduct(request):
    product_info = None
    form = ProductForm(request.POST or None, instance=product_info)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/list_edit/')

    return render(request, 'product_edit.html', {'form':form})


def editProduct(request, product_id):
    product_info = None
    try:
        product_info = get_object_or_404(Product,pk=product_id)
    except:
        product_info = None
    
    form = ProductForm(data=request.POST or None, files=request.FILES or None ,instance=product_info)
    # 주석처리 된 코드도 위의 코드와 동치입니다. (인자 순서에 따른 인자명 생략)
    # form = ProductForm(request.POST or None, request.FILES or None ,instance=product_info)
    
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/list_edit/')

    return render(request, 'product_edit.html', {'form':form})

def deleteProduct(request, product_id):
    product_info = None
    result = None
    try:
        product_info = get_object_or_404(Product,pk=product_id)
        product_info.delete()
        result = {'code':'success'}
    except:
        result = {'code':'fail'}

    result = json.dumps(result)
    
    return HttpResponse(result)