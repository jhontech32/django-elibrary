from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import Http404

from .models import TblUser
from .forms import UserForm

# Create your views here.
def index(request):
    try:
        users = TblUser.objects.all()
    except TblUser.DoesNotExists:
        raise Http404("Data not found !")
    return render(request, "Users/index.html", { 'users': users })

# DETAIL FUNCTION
def detail(request, user_id):
    try:
        user = TblUser.objects.get(pk=user_id)
        context = {
            'user': user
        }
        print('ada cteal deytai', context)
    except TblUser.DoesNotExists:
        raise Http404("Data not found !")
    return render(request, "Users/detail.html", context)

# ADD FUNCTION
def add(request):
    form = UserForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/user')
        else:
            form = UserForm()
    return render(request, "Users/add.html", {'form': form})

# DELETE FUNCTION
def delete(request, user_id):
    try:
        user = TblUser.objects.get(pk=user_id)
        user.delete()
        messages.success(request, "Success delete data !")

        return redirect('/user')
    except TblUser.DoesNotExists:
        raise Http404("Data not found !")




