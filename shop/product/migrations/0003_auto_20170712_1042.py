# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-12 01:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20170509_1802'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.FileField(upload_to='product_image')),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='Country',
            field=models.CharField(choices=[('KOR', '대한민국'), ('USA', '미국'), ('CHN', '중국'), ('JPN', '일본'), ('TWN', '대만'), ('VNM', '베트남'), ('DEU', '독일'), ('FRA', '프랑스'), ('GBR', '영국'), ('ITA', '이탈리아')], default='KOR', max_length=3),
        ),
        migrations.AddField(
            model_name='productimage',
            name='Product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product'),
        ),
    ]