# pages/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Page
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .forms import PageForm

def site_home_view(request):
  
    return render(request, 'pages/site_home.html')

class AboutView(TemplateView):
    template_name = "pages/about.html" 

 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Acerca de El Taller Interior"
       
        return context

class PageListView(ListView):
    model = Page                     # Modelo a listar
    template_name = 'pages/page_list.html' # Plantilla a usar
    context_object_name = 'pages'    # Nombre de la lista en la plantilla
    ordering = ['-publication_date'] # Ordenar por fecha más reciente
    # paginate_by = 5 # Opcional: para paginación futura    

class PageDetailView(DetailView):
    model = Page
    template_name = 'pages/page_detail.html'
    context_object_name = 'page' # Nombre del objeto en la plantilla

# Vista para /pages/create/
class PageCreateView(LoginRequiredMixin, CreateView):
    model = Page                # Modelo a crear
    form_class = PageForm       # Formulario a usar
    template_name = 'pages/page_form.html' # Plantilla para el formulario
    # URL a la que redirigir después de crear exitosamente
    success_url = reverse_lazy('page_list')

    # Asigna automáticamente el autor al crear la página
    def form_valid(self, form):
        form.instance.author = self.request.user # Asigna el usuario logueado
        return super().form_valid(form) # Continúa con el guardado normal
    

class PageUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Page
    form_class = PageForm
    template_name = 'pages/page_form.html' # Reutiliza la misma plantilla

    # Verifica si el usuario actual es el autor de la página
    def test_func(self):
        page = self.get_object() # Obtiene el objeto Page que se está editando
        return self.request.user == page.author # Devuelve True si el usuario es el autor

    # Define a dónde ir después de editar exitosamente
    def get_success_url(self):
         # Pasa el 'pk' del objeto actual a la URL de detalle
         return reverse_lazy('page_detail', kwargs={'pk': self.object.pk})

class PageDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Page
    template_name = 'pages/page_confirm_delete.html' # Plantilla de confirmación
    # URL a la que redirigir después de borrar exitosamente
    success_url = reverse_lazy('page_list')

    # Misma verificación de autor que en UpdateView
    def test_func(self):
        page = self.get_object()
        return self.request.user == page.author