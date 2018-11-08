from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from .views import index,registro,login,admin,listarperrito,model_form_upload,Eliminar,mascota_edit,adopcion

from . import views

urlpatterns = [
    path('', index,name='index'),
    path('formulario/',registro,name='reg'), #al colocar en el navegador "registro" ira al metodo de la view llamado registro, y a futuro para llamarlo desde una pagina web le damos un nombre name='reg'  
    
    path('login/', login,name='log'),
    
    path('registroperro/', model_form_upload,name='per'),
    path('administracion/', admin,name='ad'),
    path('listarperro/', listarperrito,name='lis'),
    path('adopcion/', adopcion,name='adop'),
     
   
  
    url(r'^actualizar/(?P<id_perro>\w+)$', mascota_edit,name='act'),
    url(r'^Eliminar/(?P<id_perro>\w+)$', Eliminar,name='eli'),

    
   
 
    
]