from django.urls import path
from .views import *
app_name = 'noel'
urlpatterns = [
   path('noel', noel, name='noel_1'),
 
]
