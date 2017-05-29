# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from . import models

#admin.site.register(models.Product)
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
	exclude = []
	list_display = ['Name', 'Price', 'Stock', 'Country', 'Abstraction']