from django import forms
from django.core.exceptions import ValidationError
import re
from core.models import Contacto

# class ContactoForm(forms.Form):
class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = ['nombre', 'email', 'mensaje']
    telefono = forms.CharField(max_length=12)
    # nombre = forms.CharField(
    #     min_length=3,
    #     widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu nombre'})
    # )
    # email = forms.EmailField(
    #     widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'correo@ejemplo.com'})
    # )
    # mensaje = forms.CharField(
    #     widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3})
    # )

    # edad = forms.CharField(
    #     widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3})
    # )



    # Validación de Backend
    def clean_mensaje(self):
        data = self.cleaned_data['mensaje']
        if "spam" in data.lower():
            raise ValidationError("No se permite contenido publicitario.")
        return data
    
    def clean_email(self):
        data = self.cleaned_data['email']
        if "@utez.edu.mx" not in data:
            raise ValidationError("Solo piuedes registrar correos de la utez")
        return data