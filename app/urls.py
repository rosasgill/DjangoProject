from django.urls import path
from . import views
from .forms import AuthorForm, CategoryForm, PublicadoForm


urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('items/new/', views.item_create, name='item_create'),
    path('items/edit/<int:pk>/', views.item_update, name='item_update'),
    path('items/delete/<int:pk>/', views.item_delete, name='item_delete'),

    path('authors/', views.author_list, name='author_list'),
    path('authors/create/', views.author_create, name='author_create'),
    path('authors/<int:pk>/edit/', views.author_update, name='author_update'),
    path('authors/<int:pk>/delete/', views.author_delete, name='author_delete'),

    path('category/', views.category_list, name='category_list'),
    path('category/new/', views.category_create, name='category_create'),
    path('category/edit/<int:pk>/', views.category_update, name='category_update'),
    path('category/delete/<int:pk>/', views.category_delete, name='category_delete'),

    path('publicado/', views.publicado_list, name='publicado_list'),
    path('publicado/create/', views.publicado_create, name='publicado_create'),
    path('publicado/edit/<int:pk>/', views.publicado_update, name='publicado_update'),
    path('publicado/delete/<int:pk>/', views.publicado_delete, name='publicado_delete'),
]
