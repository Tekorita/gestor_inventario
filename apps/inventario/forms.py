from django import forms
from apps.inventario.models import Inventario

class InventarioForm(forms.ModelForm):
    class Meta:
        model = Inventario

        fields = [
            'descripcion',
            'cantidad',
            'fecha_ingreso',    
        ]
        labels = {
            'descripcion':'Descripcion',
            'cantidad':'Cantidad',
            'fecha_ingreso':'Fecha de ingreso',            
        }
        widgets = {
            'descripcion':forms.TextInput(attrs={'class':'form-control'}),
            'cantidad':forms.TextInput(attrs={'class':'form-control'}),
            'fecha_ingreso':forms.TextInput(attrs={'class':'datepicker'}),
        }