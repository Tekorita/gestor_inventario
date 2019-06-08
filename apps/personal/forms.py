from django import forms
from apps.personal.models import Personal

class PersonalForm(forms.ModelForm):
    class Meta:
        model = Personal

        fields = [
            'nombre',
            'apellido',
            'cargo',
        ]
        fields = { 
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'cargo': 'Cargo',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellido': forms.TextInput(attrs={'class':'form-control'}),
            'cargo': forms.TextInput(attrs={'class':'form-control'}),            
        }

    class Meta:
        model = Personal

        fields = [
            'nombre',
            'apellido',
            'cargo',
        ]
        fields = { 
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'cargo': 'Cargo',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellido': forms.TextInput(attrs={'class':'form-control'}),
            'cargo': forms.TextInput(attrs={'class':'form-control'}),            
        }

