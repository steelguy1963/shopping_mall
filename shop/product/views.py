# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render
from models import Product

# Create your views here.

def listProduct(request):
	pList = Product.objects.all()
	return render(request, 'list.html', {'pList':pList})

def showProduct(request, product_id):
	pShow = get_object_or_404(Product, pk=product_id)
	return render(request, 'product.html', {'pShow':pShow})