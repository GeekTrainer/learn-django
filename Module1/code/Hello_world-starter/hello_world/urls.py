# [TODO]: Add the code below to create the URLconf for the app

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]