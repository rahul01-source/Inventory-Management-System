from django.shortcuts import render, redirect, get_object_or_404
from .models import *

from .forms import *
from .models import *



# Create your views here.
def index(request):
    return render (request, 'index.html')


def display_Laptops(request):
    items = Laptop.objects.all ()

    context = {
        'items': items,
        'header': 'Laptops'
    }

    return render (request, 'index.html', context)


def display_desktops(request):
    items = Desktop.objects.all ()

    context = {
        'items': items,
        'header': 'Desktops'
    }

    return render (request, 'index.html', context)


def display_mobiles(request):
    items = Mobile.objects.all ()

    context = {
        'items': items,
        'header': 'Mobiles'
    }
    return render (request, 'index.html', context)  # 3arguments


def add_laptop(request):
    if request.method == "POST":
        form = Laptopform (request.POST)

        if form.is_valid ():
            form.save ()
        return redirect ('index')
    else:
        form = Laptopform ()
        return render (request, 'add_new.html', {'form': form})


def add_desktop(request):
    if request.method == "POST":
        form = Desktopform (request.POST)

        if form.is_valid ():
            form.save ()
        return redirect ('index')
    else:
        form = Desktopform ()
        return render (request, 'add_new.html', {'form': form})


def add_mobile(request):
    if request.method == "POST":
        form = Mobileform (request.POST)

        if form.is_valid ():
            form.save ()
        return redirect ('index')
    else:
        form = Mobileform ()
        return render (request, 'add_new.html', {'form': form})


def edit_device(request,pk, model, cls):
    item = get_object_or_404(model, pk=pk)

    if request.method == "POST":
        form = cls (request.POST, instance=item)

        if form.is_valid ():
            form.save ()
        return redirect ('index')

    else:
        form =cls(instance=item)

        return render(request,'edit_item.html',{'form' : form})

def edit_laptop(request, pk):
    return edit_device(request, pk, Laptop, Laptopform)

def edit_desktop(request, pk):
    return edit_device(request, pk, Desktop, Desktopform)

def edit_mobile(request, pk):
    return edit_device(request, pk, Mobile, Mobileform)


def delete_laptop(request, pk):

    Laptop.objects.filter(id=pk).delete()

    items =Laptop.objects.all()

    context ={

        'items' : items
    }

    return render(request, 'index.html', context)


def delete_desktop(request, pk):
    Desktop.objects.filter (id=pk).delete ()

    items = Desktop.objects.all ()

    context = {

        'items': items
    }

    return render (request, 'index.html', context)


def delete_mobile(request, pk):
    Mobile.objects.filter (id=pk).delete ()

    items = Mobile.objects.all ()

    context = {

        'items': items
    }

    return render (request, 'index.html', context)


















