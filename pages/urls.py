# pages/urls.py
from django.urls import path
from .views import PageListView, PageDetailView, AboutView, PageCreateView, PageUpdateView, PageDeleteView

urlpatterns = [
    path('', PageListView.as_view(), name='page_list'),
    path('about/', AboutView.as_view(), name='about'),
    path('create/', PageCreateView.as_view(), name='page_create'),
    path('<int:pk>/', PageDetailView.as_view(), name='page_detail'),
    path('<int:pk>/delete/', PageDeleteView.as_view(), name='page_delete'),
    path('<int:pk>/update/', PageUpdateView.as_view(), name='page_update')
]