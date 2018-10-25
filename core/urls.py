from django.contrib import admin
from django.urls import path
from .views import index,registro

urlpatterns = [
    path('', index,name='index'),
    path('registro/',registro,name='reg'), #al colocar en el navegador "registro" ira al metodo de la view llamado registro, y a futuro para llamarlo desde una pagina web le damos un nombre name='reg'  

]