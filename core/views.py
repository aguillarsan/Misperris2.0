from django.shortcuts import render
from .models import Cliente 
def index(request):
    return render(request,'core/index.html')
    


##def registro(request):
  #  cliente= Cliente.objects.alls()
   ##    rut=request.POST.get("rut","")
     #  nombres=request.POST.get("nombres","")
      #  apellidos=request.POST.get("apellidos","")
      #  telefono=request.POST.get("telefono","")
        #fechaNaci=request.POST.get("fechaNaci","")
        #region=request.POST.get("region","")
       #ciudad=request.POST.get("ciudad","")
       # tipoViv=request.POST.get("tipoViv","")
       # correo=request.POST.get("correo","")
       
        #cli= Cliente(
            #nombres=nombres,
            #apellidos=apellidos,
            #rut=rut,
           # telefono=telefono,
          #  fechaNaci=fechaNaci,
         #   region=region,
        #    ciudad=ciudad,
       #     tipoViv=tipoViv,
      #    cli.save() 
   #     return render(request,'core/formulario.html',{'cli':cliente,'grabo':True})
  ##  else:       
##        return render(request,'core/formulario.html',{'cli':cliente,'grabo':False})
###