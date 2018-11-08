from django.shortcuts import render, redirect
from .models import Cliente,Perro,Raza,Sexo,Disponibilidad
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import get_object_or_404
from django.http import HttpResponse




from .forms import DocumentForm,CliForm



def index(request):
    return render(request,'core/index.html')
    
def Eliminar(request,id_perro):
    perro = Perro.objects.get(id=id_perro)
    if request.method == 'POST':
        perro.delete()
        pe=Perro.objects.all()    
        return render(request,'core/listarperro.html',{'perros':pe})
    
    return render( request, 'core/Eliminar.html', {'perro': perro}) 

    



def mascota_edit(request,id_perro):
    perro=Perro.objects.get(id=id_perro)
    if request.method == 'GET':
        form = DocumentForm(instance=perro)
    else:
        form = DocumentForm(request.POST, instance=perro)
        if form.is_valid():
            form.save()
            pe=Perro.objects.all()    
            return render(request,'core/listarperro.html',{'perros':pe})
   
    return render( request, 'core/registroperro.html', {
        'form': form
    }) 
    
   
     

   





def login(request):
  return render(request,'core/login.html')    






def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            pe=Perro.objects.all()    
            contexto = {'perros':pe}
            return render(request,'core/listarperro.html', contexto) 
          
           
            
    else:
        form = DocumentForm()
    return render(request, 'core/registroperro.html', {
        'form': form
    })


def registro(request):
    if request.method == 'POST':
        form = CliForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            pe=Cliente.objects.all()    
            return render(request,'core/index.html') 
          
           
            
    else:
        form = CliForm()
    return render(request, 'core/formulario.html', {
        'form': form
    })








def admin(request):
    return render(request,'core/administracion.html')



def listarperrito(request):
    pe=Perro.objects.all()    
    contexto = {'perros':pe}
    return render(request,'core/listarperro.html', contexto)



def adopcion(request):
    pe=Perro.objects.all()    
    contexto = {'per':pe}
    return render(request,'core/adopcion.html', contexto)

      




    

 