from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="book"),
    path('add', views.add, name="addBook"),
    path('detail/<int:book_id>', views.detail, name="detailBook"),
    path('update/<int:book_id>', views.update, name="updateBook"),
    path('delete/<int:book_id>', views.delete, name="deleteBook")
]