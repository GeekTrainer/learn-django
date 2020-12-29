# [TODO]: Add the code below to create the URLconf for the app

from django.urls import path
from . import views

urlpatterns = [
    path('home', views.index, name='index'),
    # [TODO]: Make sure this path is in urlpattherns and add the path for ShelterList ListView
    path('shelter_list', views.ShelterList.as_view(), name='ShelterList'),
    # [TODO]: Make sure this path is in urlpattherns and add the path for ShelterDetail DetailView
    path('<int:pk>', views.ShelterDetail.as_view(), name='ShelterDetail'),
    path('shelter_spotlight', views.spotlight, name='spotlight'),
]