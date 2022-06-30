from django.forms import ModelForm
from .models import TblBook

class BookForm(ModelForm):
    class Meta:
        model = TblBook
        fields = ('title', 'description', 'author', 'picture')
        labels = {
            'title': 'Title',
            'description': 'Description',
            'author': 'Author',
            'picture': 'Picture'
        }
