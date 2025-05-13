from django import forms
from .models import Page

class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        # Selecciona los campos que el usuario llenará en el formulario
        # Excluimos 'author' (se asignará automáticamente en la vista)
        # Excluimos 'publication_date' (se asignará automáticamente)
        fields = ['title', 'subtitle', 'content', 'image']

        # Opcional: Añadir widgets para estilizar con CSS (ej. Bootstrap)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título de la página'}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subtítulo (opcional)'}),
            # 'content' usará automáticamente el widget de CKEditor
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }