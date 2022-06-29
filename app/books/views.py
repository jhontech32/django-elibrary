from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib import messages

from .models import TblBook
from .forms import BookForm

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
    form = BookForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/book')
        else:
            form = BookForm()

    return render(request, "Books/add.html", {'form': form})

# UPDATE FUNCTION
def update(request, book_id):
    # wajib initialize lebih dahulu
    # form = BookForm()

    try:
        book = TblBook.objects.get(pk=book_id)
    except TblBook.DoesNotExist:
        raise Http404('Data not found!')

    # pengecekan action
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, "Success update data !")
            return redirect('/book')
    else:
        form = BookForm(instance=book)
    return render(request, "Books/update.html", {'form': form})

# DELETE FUNCTION
def delete(request, book_id):
    try:
        book = TblBook.objects.get(pk=book_id)
        book.delete()
        messages.success(request, 'Success deleted data !')
        return redirect("/book")
    except:
        raise Http404('Data not found !')
