from .views import index, inicio
from django.urls import path

urlpatterns = [
    path('hello/', index),
    path('', inicio),
]
