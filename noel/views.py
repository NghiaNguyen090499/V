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
    
