from django import forms
from .models import Author, Category, Post

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'email', 'bio'] # Campos a incluir en el formulario

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author', 'category']
        # Opcional: Usar widgets para mejorar la experiencia
        widgets = {
            'publication_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class SearchForm(forms.Form):
    query = forms.CharField(label='Buscar Posts por Título', max_length=100)