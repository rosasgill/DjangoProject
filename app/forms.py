from django import forms
from .models import Item, Author, Publicado, Category

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description']

class PublicadoForm(forms.ModelForm):
    class Meta:
        model = Publicado
        fields = ['date', 'mes', 'ano', 'description']

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'idade', 'nacionalidade']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']

