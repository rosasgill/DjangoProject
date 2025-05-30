from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm

def item_list(request):
    items = Item.objects.all()
    return render(request, 'app/item_list.html', {'items': items})

def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm()
    return render(request, 'app/item_form.html', {'form': form})

def item_update(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm(instance=item)
    return render(request, 'app/item_form.html', {'form': form})

def item_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('item_list')
    return render(request, 'app/item_confirm_delete.html', {'item': item})





from django.shortcuts import render, redirect, get_object_or_404
from .models import Publicado
from .forms import PublicadoForm


def publicado_list(request):
    items = Item.objects.all()
    return render(request, 'app/publicado_list.html', {'publicado': Publicado})

def publicado_create(request):
    if request.method == 'POST':
        form = PublicadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = Publicado()
    return render(request, 'app/publicado.html', {'form': form})

def publicado_update(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        form = Publicado(request.POST, instance= Publicado)
        if form.is_valid():
            form.save()
            return redirect('publicado')
    else:
        form = Publicado(instance=Publicado)
    return render(request, 'app/publicado_form.html', {'form': form})

def publicado_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        Publicado.delete()
        return redirect('publicado')
    return render(request, 'app/publicado_confirm_delete.html', {'publicado': Publicado})
