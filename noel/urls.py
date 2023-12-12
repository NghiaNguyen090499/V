from django.urls import path
from . import views

urlpatterns = [
    path('noel', views.index, 'noel'),
 
]
