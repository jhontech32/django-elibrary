from django.shortcuts import render, redirect
from django.contrib import messages

from app.books.models import TblBook
from .models import TblTransaction

from .forms import TransForm

# Create your views here.
def index(request):
    return render(request, "Transactions/index.html")

# ADD FUNCTION
def add(request):
    books = TblBook.objects.all()
    # Begin initialize
    form = TransForm()
    if request.method == 'POST':
        form = TransForm(request.POST)
        print('')
        form.save()
        messages.success(request, "Success add data !")
        return redirect('/transaction')
    else:
        form: TransForm()
    return render(request, "Transactions/add.html", {'form': form, 'books': books})