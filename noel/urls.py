from django.urls import path
from .views import *
app_name = 'noel'
urlpatterns = [
   path('noel', noel, name='noel_1'),
   path('detail/<int:pk>/',detail, name='detail'),
   path('a',handle, name='a'),
   path('login',dang_nhap, name='login'),
 
]
