from django.contrib import admin
from .models import Cliente,Login,Region,TipoVivienda,Ciudad
 

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Login)
admin.site.register(Region)
admin.site.register(TipoVivienda)
admin.site.register(Ciudad)
