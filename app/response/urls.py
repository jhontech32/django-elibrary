from django.urls import path
from . import views

urlpatterns = [
    path('', views.page404, name="404")
]