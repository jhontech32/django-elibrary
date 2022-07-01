from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib import messages
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from .models import TblBook
from .forms import BookForm

import os

# Create your views here.
def index(request):
    books = TblBook.objects.all().order_by('-id')
    return render(request, "Books/index.html", { 'books': books })

# DETAIL FUNCTION
def detail(request, book_id):
    try:
        book = TblBook.objects.get(pk=book_id)
        context = {
            'book': book
        }
    except TblBook.DoesNotExists:
        raise Http404('Data not found !')
    return render(request, "Books/detail.html", context)

# ADD FUNCTION
def add(request):
    form = BookForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            messages.success(request, "Success add data !")
            return redirect('/book')
        else:
            form = BookForm()
    return render(request, "Books/add.html", {'form': form})

# UPDATE FUNCTION
def update(request, book_id):
    book = TblBook.objects.get(id=book_id)
    form = BookForm(request.POST, request.FILES, instance=book)
    if form.is_valid():
        form.save()
        return redirect('/book')
    form = BookForm(instance=book)
    return render(request, "Books/update.html", {'form': form, 'book': book})

# DELETE FUNCTION
def delete(request, book_id):
    try:
        book = TblBook.objects.get(pk=book_id)
        book.delete()
        messages.success(request, 'Success deleted data !')
        return redirect("/book")
    except:
        raise Http404('Data not found !')
