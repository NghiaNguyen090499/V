from django.urls import path
from .views import *
app_name = 'noel'
urlpatterns = [
   path('noel', noel, name='noel_1'),
   path('detail/<int:pk>/',detail, name='detail'),
   path('test',handle, name='a'),
 
]
