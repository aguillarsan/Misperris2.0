from django import forms

from .models import Perro,Cliente


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Perro
        fields = [
            'nombres',
            'Sexo',
            'Descripcion',
            'Raza',
            'Estado',
            'media' 
        ]
        labels = {
            'nombres': 'Nombre',
            
            'media': 'Foto',
        }

        widgets = {

            'nombres': forms.TextInput(attrs={'class':'form-control'}),
            'Descripcion': forms.TextInput(attrs={'class':'form-control'}),
            
        }

class CliForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'rut',
            'nombres',
            'apellidos',
            'FechaNaci',
            'Telefono',
            'Correo', 
            'IdCiudad',
            'IdRegion',
            'IdTipoViv',
        ]
        labels = {
            'IdCiudad': 'Ciudad',
            
            'IdRegion': 'Region',
            'IdTipoViv': 'Tipo vivienda',
        }

       





        
        