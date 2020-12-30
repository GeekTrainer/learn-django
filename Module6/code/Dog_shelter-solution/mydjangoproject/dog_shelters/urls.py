# [TODO]: Add the code below to create the URLconf for the app

from django.urls import path
from . import views

urlpatterns = [
    path('home', views.index, name='index'),
    # [TODO]: Add the path below for our ShelterList ListView
    path('shelter_list', views.ShelterList.as_view(), name='ShelterList'),
    # [TODO]: Add the path below for our ShelterDetail DetailView
    path('<int:pk>', views.ShelterDetail.as_view(), name='ShelterDetail'),
    path('shelter_spotlight', views.spotlight, name='spotlight'),
    path('contact', views.contactForm, name='contactForm'),
    path('thank_you', views.thankyou, name='thankyou'),
    # [TODO]: Add the path below for our Shelter CreateView
    path('shelter_form', views.CreateShelter.as_view(), name='CreateShelter'),
    # [TODO]: Add the belows for our Shelter UpdateView, DeleteView and template page to call these functions
    path('<pk>/update', views.UpdateShelter.as_view(), name='UpdateShelter'),
    path('<pk>/delete', views.DeleteShelter.as_view(), name='DeleteShelter'),
    path('update_delete_shelters', views.ShelterEdits.as_view(), name='ShelterEdits'),
]