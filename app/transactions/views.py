from django.shortcuts import render, redirect

# from .models import TblTransaction
from .forms import TransForm

# Create your views here.
def index(request):
    return render(request, "Transactions/index.html")

# ADD FUNCTION
def add(request):
    # Begin initialize
    form = TransForm()
    if request.method == 'POST':
        form = TransForm(request.POST)
        form.save()
        return redirect('/transaction')
    else:
        form: TransForm()
    return render(request, "Transactions/add.html", {'form': form})