# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from . import models

# admin.StackedInline
class ProductImageInline(admin.TabularInline):
	exclude = []
	extra = 1
	model = models.ProductImage

#admin.site.register(models.Product)
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
	exclude = []
	inlines = [
		ProductImageInline
	]
	list_display = ['Name', 'Price', 'Stock', 'Country', 'Abstraction']

@admin.register(models.ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
	exclude = []