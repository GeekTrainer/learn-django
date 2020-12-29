from django.shortcuts import render

def thankyou(request):
    return render(request, 'thank_you.html')

# [TODO] Create your views
from dog_shelters.models import Shelter, Dog

def index(request):

    # Generate count of dog shelters in database
    num_shelters = Shelter.objects.all().count()

    # Generate count of dogs ready for adoption in database
    num_dogs = Dog.objects.all().count()        

    return render(request, 'index.html', {'num_shelters': num_shelters, 'num_dogs': num_dogs})

# [TODO] Add Generic Listview
from django.views.generic import ListView

class ShelterList(ListView):
    model = Shelter
    context_object_name = 'my_shelter_list'   # your own name for the list as a template variable
    template_name = "shelter_list.html"

# [TODO] Add Generic Detailview
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404

class ShelterDetail(DetailView):
   def get(self, request, *args, **kwargs):
        shelter = get_object_or_404(Shelter, pk=kwargs['pk'])
        context = {'shelter': shelter}
        return render(request, 'shelter_details.html', context)

def spotlight(request):

    # Generate count of dog shelters in database
    get_shelters = Shelter.objects.all()

    # Generate count of dogs ready for adoption in database
    get_dogs = Dog.objects.all()

    return render(request, 'shelter_spotlight.html', {'get_shelters': get_shelters, 'get_dogs': get_dogs})

# [TODO] Create view for ClientForm


# [TODO] Develop CreateView generic view for form


# [TODO] Create ListView to add shelters to update_delete_shelters template


# [TODO] Develop UpdateView and DeleteView for forms
