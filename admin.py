from django.contrib import admin
from .models import Cliente,Login,Region,TipoVivienda,Ciudad,Raza,Perro,Sexo,Disponibilidad
 

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Login)
admin.site.register(Region)
admin.site.register(TipoVivienda)
admin.site.register(Ciudad)
admin.site.register(Raza)
admin.site.register(Perro)
admin.site.register(Sexo)
admin.site.register(Disponibilidad)