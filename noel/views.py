from django.shortcuts import render
from noel.models import *
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


def handle(self, *args, **options):
    csv_file = 'noel_subcategory.csv'  # Đường dẫn đến file CSV của bạn

    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            subcategory, created = SubCategory.objects.get_or_create(
                id=row['id'],
                name=row['name'],
                defaults={'image': row['image']}
            )

        

    self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
