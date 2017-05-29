# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Product(models.Model):
	Name = models.CharField(max_length=50)
	Thumbnail = models.FileField(upload_to='product')
	Price = models.IntegerField()
	Stock = models.IntegerField(null=True)
	Country = models.CharField(max_length=50, null=True, blank=True)
	Abstraction = models.CharField(max_length=500, null=True, blank=True)
