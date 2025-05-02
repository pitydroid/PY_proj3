# messaging/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Bandeja de entrada (lista de conversaciones)
    path('', views.inbox_view, name='inbox'),
    # Lista de usuarios para iniciar conversación
    path('users/', views.user_list_view, name='user_list'),
    # Detalle de conversación con un usuario específico
    path('conversation/<str:username>/', views.conversation_detail_view, name='conversation_detail'),
]