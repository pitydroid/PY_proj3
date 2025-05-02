# messaging/forms.py
from django import forms

class MessageForm(forms.Form):
    content = forms.CharField(
        label="", # Sin etiqueta visible
        widget=forms.Textarea(attrs={
            'rows': 3,
            'class': 'form-control', # Para estilo Bootstrap si usas
            'placeholder': 'Escribe tu mensaje aquí...'
            })
    )