from django.shortcuts import render, redirect, get_object_or_404
from .models import Item, Category
from .forms import ItemForm, CategoryForm

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

<<<<<<< HEAD




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
=======
def category_list(request):
    categorys = Category.objects.all()
    return render(request, 'app/category_list.html', {'categorys': categorys})

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'app/category_form.html', {'form': form})

def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'app/category_form.html', {'form': form})

def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'app/category_confirm_delete.html', {'category': category})
>>>>>>> bcd0cac47a898c87bf84cb82db4d004363d84a5b
