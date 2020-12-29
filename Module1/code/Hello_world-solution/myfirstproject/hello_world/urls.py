# [TODO]: Add the code below in the newly created file urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]