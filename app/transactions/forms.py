from django.forms import ModelForm
from django import forms

from .models import TblTransaction

class TransForm(ModelForm):
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
        fields = ('name', 'book', 'startDate', 'endDate')
        labels = {
            'name': 'Nama',
            'book': 'Buku',
            'startDate': 'Start Date',
            'endDate': 'End Date'
        }
