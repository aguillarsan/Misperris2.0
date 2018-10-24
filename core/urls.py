from django.contrib import admin
from django.urls import path
from .views import index,registro

urlpatterns = [
    path('', index,name='home'),
    path('formulario/',registro,name='registro')
    

]