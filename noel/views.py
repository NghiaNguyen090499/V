from django.shortcuts import render, redirect
from noel.models import *
import csv
from django.http import HttpResponse
from VoteApp.settings import MEDIA_ROOT
import time
from datetime import datetime
# Create your views here.


def dang_nhap(request):
    result_login=''
    if request.POST.get('btnDangNhap'):
        print('a')

        name = request.POST.get('name')
        print(name)
        mat_khau = request.POST.get('mat_khau')
        print(mat_khau)
        
        if name =='thucphanhyeudau' and mat_khau=='02122023':
            request.session['name'] = name
            request.session['mat_khau'] = mat_khau
           
            return redirect('noel:noel_1')
        else:
            result_login = '''
            <div class="alert alert-danger" role="alert">
                Đăng nhập thất bại. Vui lòng kiểm lại thông tin
            </div>
            '''
    return render(request, 'noel/login.html',{
       
        })
    

def noel(request):
    
    if 'name'  in request.session and 'mat_khau' in request.session :
    
        content = SubCategory.objects.filter(id__lt=SubCategory.objects.last().id)
        now = Product.objects.filter(subcategory_id=7)
        
        print(content)
        message=''
        if request.method == 'POST' :
            text = request.POST.get('love')
            print(text)
            Text.objects.create(name=text)
            message='Anh nhận được rồi, cám ơn bé nhá'
        return render(request, "noel/index.html",{ 'content':content,'message':message,'now':now})
    else:
        return redirect('noel:login')


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
                id=row['id'],
                defaults={'name': row['name'], 'image': row['image'],'subcategory_id':row['subcategory_id']}
            )
            

    return HttpResponse('Data updated successfully!')



# views.py

from .models import Achievement
from .forms import AchievementFormSet




def checklist(request):
    
    if request.method == 'POST':
        formset = AchievementFormSet(request.POST, queryset=Achievement.objects.all())
        print(formset)
        if formset.is_valid():
            formset.save()
    else:
        formset = AchievementFormSet(queryset=Achievement.objects.all())

    return render(request, 'noel/checklist.html', {'formset': formset})

 

