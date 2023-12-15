from django.shortcuts import render
from noel.models import *
import csv
from django.http import HttpResponse
from VoteApp.settings import MEDIA_ROOT
import time
from datetime import datetime
# Create your views here.

def noel(request):
    content = SubCategory.objects.filter(id__lt=SubCategory.objects.last().id)

    print(content)
    message=''
    if request.method == 'POST' :
        text = request.POST.get('love')
        print(text)
        Text.objects.create(name=text)
        message='Anh nhận được rồi, cám ơn bé nhá'
    return render(request, "noel/index.html",{ 'content':content,'message':message})


def detail(request, pk):
    # Danh mục sản phẩm
    subcategories = SubCategory.objects.order_by('name')

    products = Product.objects.filter(subcategory=pk)
    subcategory_name = str(SubCategory.objects.get(pk=pk))

    return render(request, 'noel/detail.html', {
        'subcategories': subcategories,
        'products': products,
        'subcategory_name': subcategory_name,
    })
    
# mycakes/management/commands/load_data.py

import csv
from django.core.management.base import BaseCommand
from noel.models import SubCategory, Product



def handle(request):
    csv_file_path = MEDIA_ROOT + 'mycakes/noel_subcategory.csv'
 
    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            subcategory, created = SubCategory.objects.get_or_create(
                id=row['id'],
                defaults={'name': row['name'], 'image': row['image']}
            )
    csv_file_path = MEDIA_ROOT + 'mycakes/noel_product.csv'
 
    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            product, created = Product.objects.get_or_create(
                subcategory=subcategory,
                defaults={'name': row['name'], 'image': row['image']}
            )
            

    return HttpResponse('Data updated successfully!1')

