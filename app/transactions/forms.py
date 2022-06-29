from django.forms import ModelForm
from django import forms

from .models import TblTransaction
from app.books.models import TblBook

# STATES = [
#     'ID',
#     'MG',
#     'SP',
#     'RJ'
# ]

STATES = [
    {'BM', 'Bumi Manusia'},
    {'HP', 'Harry Potter'},
    {'FN', 'Fangirl'},
    {'TG', 'The Hunger Games'}
]

class TransForm(ModelForm):
    listBook = []
    # LIST BOOKS
    # books = TblBook.objects.all()
    books = TblBook.objects.values_list('title', flat=True)
    print('booktop', books)

    for data in books:
        listBook.append(data)

    print('hasil for lloop', listBook)

    book = forms.ChoiceField(choices=STATES)
    startDate = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date'}
        )
    )
    endDate = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date'}
        )
    )

    class Meta:
        model = TblTransaction
        fields = '__all__'
        labels = {
            'name': 'Nama',
            'book': 'Buku',
            'startDate': 'Start Date',
            'endDate': 'End Date'
        }
