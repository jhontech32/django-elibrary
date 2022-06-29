from django.forms import ModelForm, Textarea, DateInput, NumberInput
from app.models.cbreim import *
from django import forms


class CbreimForm(ModelForm):
    phone = forms.CharField(required=True, label='')
    address = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 3}), label='', required=False)
    description = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 3}), label='', required=False)

    class Meta:
        model = Cbreim
        fields = '_all_'
        labels = {
            'reimbursement_no': '',
            'customer': '',
            'company': '',
            'warehouse': '',
            'reimbursement_date': '',
            'dest_bank': '',
            'src_bank': '',
            'address': '',
            'status': '',
            'outlet': '',
            'collector': '',
            'bank': ''
        }

        widgets = {
            'address': Textarea(attrs={'cols': 50, 'rows': 5}),
            'due_date': DateInput(),
            'reimbursement_date': DateInput(),
            'pmt_net_days': NumberInput(attrs={'min': 1}),
            'description': Textarea(attrs={'cols': 50, 'rows': 5})
        }