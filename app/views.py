from django.shortcuts import render, redirect, get_object_or_404
from .models import Item, Author, Category, Publicado
from .forms import ItemForm, AuthorForm, CategoryForm, PublicadoForm


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


def publicado_list(request):
    publicados = Publicado.objects.all()
    return render(request, 'app/publicado_list.html', {'publicados': publicados})

def publicado_create(request):
    if request.method == 'POST':
        form = PublicadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('publicado_list')
    else:
        form = PublicadoForm()
    return render(request, 'app/publicado_form.html', {'form': form})


def publicado_update(request, pk):
    publicado = get_object_or_404(Publicado, pk=pk)
    if request.method == 'POST':
        form = PublicadoForm(request.POST, instance=publicado)
        if form.is_valid():
            form.save()
            return redirect('publicado_list')
    else:
        form = PublicadoForm(instance=publicado)
    return render(request, 'app/publicado_form.html', {'form': form})

def publicado_delete(request, pk):
    publicado = get_object_or_404(Publicado, pk=pk)
    if request.method == 'POST':
        publicado.delete()
        return redirect('publicado_list')
    return render(request, 'app/publicado_confirm.html', {'publicado': publicado})

# Antonio Gabriel
def author_list(request):
    authors = Author.objects.all()
    return render(request, 'app/author_list.html', {'authors': authors})

def author_create(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author_list')
    else:
        form = AuthorForm()
    return render(request, 'app/author_form.html', {'form': form})
    # return render(request, 'app/item_form.html', {'form': form})

def author_update(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('author_list')
    else:
        form = AuthorForm(instance=author)
    return render(request, 'app/author_form.html', {'form': form})

def author_delete(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        author.delete()
        return redirect('author_list')
    return render(request, 'app/author_confirm_delete.html', {'author': author})

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

