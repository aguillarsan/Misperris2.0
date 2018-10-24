from django.db import models

# Creacion de las tablas 

class Login(models.Model):
    usuario=models.CharField(max_length=15,primary_key=True,verbose_name="login")
    contraseña=models.CharField(max_length=10)

    def __str__(self):
        return self.usuario
    


class Region(models.Model):
    IdRegion=models.IntegerField(primary_key=True,verbose_name="region")
    descripcion=models.TextField()
    def __str__(self):
        return self.descripcion
        
    
class Ciudad(models.Model):
    IdCiudad=models.IntegerField(primary_key=True,verbose_name="ciudad")
    descripcion=models.TextField()
    IdRegion=models.ForeignKey(Region,on_delete=models.CASCADE)
    def __str__(self):
        return self.descripcion

class TipoVivienda(models.Model):
    IdTipoViv=models.IntegerField(primary_key=True,verbose_name="tipoviv")
    Descripcion=models.TextField()

    def __str__(self):
        return self.Descripcion
    


class Cliente(models.Model):
    rut=models.CharField(max_length=10,primary_key=True,verbose_name="rut")
    nombres=models.TextField()
    apellidos=models.TextField()
    FechaNaci=models.DateField()
    Telefono=models.IntegerField()
    Correo=models.TextField()
    IdCiudad=models.ForeignKey(Ciudad,on_delete=models.CASCADE)
    IdRegion=models.ForeignKey(Region,on_delete=models.CASCADE)
    IdTipoViv=models.ForeignKey(TipoVivienda,on_delete=models.CASCADE)
  
    def __str__(self):
        return self.rut
    