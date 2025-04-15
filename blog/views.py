# blog/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Author, Category, Post
from .forms import AuthorForm, CategoryForm, PostForm, SearchForm

def home_view(request):
    latest_posts = Post.objects.all()[:5] # Obtener los últimos 5 posts
    search_form = SearchForm() # Incluir el form de búsqueda en el contexto
    context = {
        'latest_posts': latest_posts,
        'search_form': search_form
    }
    return render(request, 'blog/home.html', context)

def add_author_view(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirigir a una página de éxito o a la home
            # return redirect('home')
            # O usar una página de éxito genérica:
            return render(request, 'blog/success.html', {'message': 'Autor añadido correctamente!'})
    else: # Método GET
        form = AuthorForm()
    return render(request, 'blog/add_author.html', {'form': form})

def add_category_view(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'blog/success.html', {'message': 'Categoría añadida correctamente!'})
    else: # Método GET
        form = CategoryForm()
    return render(request, 'blog/add_category.html', {'form': form})

def add_post_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'blog/success.html', {'message': 'Post añadido correctamente!'})
        else:
            # Si el formulario no es válido, se volverá a renderizar con errores
            print(form.errors) # Útil para depuración en consola
    else: # Método GET
        form = PostForm()
        # Asegurarse de que haya autores y categorías para seleccionar
        if not Author.objects.exists():
             return render(request, 'blog/error.html', {'message': 'Debes añadir al menos un autor antes de crear un post.'})
        

    return render(request, 'blog/add_post.html', {'form': form})


def search_view(request):
    query = request.GET.get('query', '') # Obtener el parámetro 'query' de la URL (GET)
    results = []
    search_form = SearchForm(request.GET or None) # Inicializa con datos GET si existen

    if query:
        # Realizar la búsqueda insensible a mayúsculas/minúsculas en el título
        results = Post.objects.filter(title__icontains=query)

    context = {
        'search_form': search_form,
        'results': results,
        'query': query,
    }
    return render(request, 'blog/search_results.html', context)
def post_detail_view(request, pk):
    # Busca el Post con la primary key (pk) especificada en la URL.
    # Si no lo encuentra, automáticamente devuelve un error 404 (Página no encontrada).
    post = get_object_or_404(Post, pk=pk)

    # Prepara el contexto para pasar el objeto 'post' a la plantilla
    context = {
        'post': post
    }
    # Renderiza la plantilla 'post_detail.html' con el contexto
    return render(request, 'blog/post_detail.html', context)
