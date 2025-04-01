from django import forms
from .models import Comentario, MensajeContacto, Cancion

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']
        widgets = {
            'texto': forms.Textarea(attrs={
                'rows': 2, 'placeholder': 'Escribe un comentario...'
            })
        }

from .models import MensajeContacto
from django import forms

class ContactoForm(forms.ModelForm):
    class Meta:
        model = MensajeContacto
        fields = ['nombre', 'correo', 'mensaje']
        widgets = {
            'mensaje': forms.Textarea(attrs={'rows': 4}),
        }


class CancionForm(forms.ModelForm):
    class Meta:
        model = Cancion
        fields = ['titulo', 'descripcion', 'archivo']

