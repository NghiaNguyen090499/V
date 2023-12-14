from django.shortcuts import render
from noel.models import *
from django.http import HttpResponse
from VoteApp.settings import MEDIA_ROOT
# Create your views here.
def noel(request):
    content = SubCategory.objects.all()
    products = Product.objects.get(id=1)
    print(products)
    return render(request, "noel/index.html",{'product':products, 'content':content})


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
    

import csv
from django.core.management.base import BaseCommand
from noel.models import SubCategory, Product

# mycakes/management/commands/load_data.py


def handle(request):
    csv_file_path = MEDIA_ROOT + 'mycakes/noel_product.csv'
 
    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            subcategory_id = int(row['subcategory_id'])
            product, created = Product.objects.get_or_create(
                id=row['id'],
                defaults={
                    'name': row['name'],
                    'image': row['image'],
                    'public_day': row['public_day'],
                    'subcategory': subcategory_id
                }
            )
    
        
            

    return HttpResponse('Data updated successfully!')


