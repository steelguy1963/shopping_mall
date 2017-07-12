# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

COUNTRY_CHOICE = (
	('KOR','대한민국'),
	('USA','미국'),
	('CHN','중국'),
	('JPN','일본'),
	('TWN','대만'),
	('VNM','베트남'),
	('DEU','독일'),
	('FRA','프랑스'),
	('GBR','영국'),
	('ITA','이탈리아'),
)

class Product(models.Model):
	Name = models.CharField(max_length=50)
	Thumbnail = models.FileField(upload_to='product')
	Price = models.IntegerField()
	Stock = models.IntegerField(null=True)
	Country = models.CharField(max_length=3,choices=COUNTRY_CHOICE,default='KOR')
	Abstraction = models.CharField(max_length=500, null=True, blank=True)
	
	def __str__(self):
		return self.Name

	def multiply(self):
		return self.Price * self.Stock

class ProductImage(models.Model):
	Product = models.ForeignKey(Product)
	Image = models.FileField(upload_to='product_image')
