# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('add_author/', views.add_author_view, name='add_author'),
    path('add_category/', views.add_category_view, name='add_category'),
    path('add_post/', views.add_post_view, name='add_post'),
    path('search/', views.search_view, name='search'), # Ruta para mostrar el form y resultados
    path('post/<int:pk>/', views.post_detail_view, name='post_detail'),
]