from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="user"),
    path('add', views.add, name="addUser"),
    path('detail/<int:user_id>', views.detail, name="detailUser"),
    path('delete/<int:user_id>', views.delete, name="deleteUser")
]