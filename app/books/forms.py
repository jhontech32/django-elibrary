from django.forms import ModelForm
from .models import TblBook

class BookForm(ModelForm):
    class Meta:
        model = TblBook
        fields = '__all__'
        labels = {
            'title': 'Title',
            'description': 'Description',
            'author': 'Author'
        }
