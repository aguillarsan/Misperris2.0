from __future__ import unicode_literals

from django.db import models


# Creacion de las tablas 

class Login(models.Model):
    usuario=models.CharField(max_length=15,primary_key=True,verbose_name="login")
    contraseña=models.CharField(max_length=10)

    def __str__(self):
        return self.usuario
    


class Region(models.Model):
    IdRegion=models.IntegerField(primary_key=True,verbose_name="region")
    descripcion=models.CharField(max_length=40)
    def __str__(self):
        return self.descripcion
        
    
class Ciudad(models.Model):
    IdCiudad=models.IntegerField(primary_key=True,verbose_name="ciudad")
    descripcion=models.CharField(max_length=40)
    IdRegion=models.ForeignKey(Region,on_delete=models.CASCADE)
    def __str__(self):
        return self.descripcion

class TipoVivienda(models.Model):
    IdTipoViv=models.IntegerField(primary_key=True,verbose_name="tipoviv")
    Descripcion=models.CharField(max_length=40)

    def __str__(self):
        return self.Descripcion
    
    
    def alamcenar(self):
        return self.save()   

class Cliente(models.Model):
    rut=models.CharField(max_length=10,primary_key=True,verbose_name="rut")
    nombres=models.CharField(max_length=40)
    apellidos=models.CharField(max_length=40)
    FechaNaci=models.DateField()
    Telefono=models.IntegerField()
    Correo=models.CharField(max_length=40)
    IdCiudad=models.ForeignKey(Ciudad,on_delete=models.CASCADE)
    IdRegion=models.ForeignKey(Region,on_delete=models.CASCADE)
    IdTipoViv=models.ForeignKey(TipoVivienda,on_delete=models.CASCADE)
  
    def __str__(self):
        return self.rut

    def alamcenar(self):
        return self.save()       





class Raza(models.Model):
    descripcion=models.CharField(max_length=40,primary_key=True,verbose_name="Raza")

    def __str__(self):
        return self.descripcion

    def alamcenar(self):
        return self.save()    


class Sexo(models.Model):
    tipo=models.CharField(max_length=40,primary_key=True,verbose_name="Sexo")

    def __str__(self):
        return self.tipo

    def alamcenar(self):
        return self.save()   



class Disponibilidad(models.Model):
    id_est=models.IntegerField(primary_key=True,verbose_name="idEstado")
    est=models.CharField(max_length=40,verbose_name="Disponibilidad")

    def __str__(self):
        return self.est

    def alamcenar(self):
        return self.save()          
           
    



class Perro(models.Model):
  
    
    nombres=models.CharField(max_length=40,name="nombres")
    Sexo=models.ForeignKey(Sexo,on_delete=models.CASCADE)
    Descripcion=models.CharField(max_length=500)
    Estado=models.ForeignKey(Disponibilidad,on_delete=models.CASCADE)
    Raza=models.ForeignKey(Raza,on_delete=models.CASCADE)  
    media = models.FileField(upload_to='coduments/')
  
    def __str__(self):
        return self.nombres

    def alamcenar(self):
        return self.save()   