from django import forms
from .models import Item, Publicado


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description']


from django import forms
from .models import Item

class PublicadoForm(forms.ModelForm):
    class Meta:
        model = Publicado
        fields = ['name', 'publicado']

