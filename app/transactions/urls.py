from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="transaction"),
    path('add', views.add, name="addTransaction")
]