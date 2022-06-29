from django.forms import ModelForm
from django import forms
from .models import TblUser

class UserForm(ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = TblUser
        fields = '__all__'
        labels = {
            'name': 'Name',
            'phone': 'Phone',
            'email': 'Email'
        }
