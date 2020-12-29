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
from django.http import HttpResponseRedirect

from .forms import ClientForm

def contactForm(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        # check if form is valid:
        if form.is_valid():
            # code to process data from from as appropiate
            return HttpResponseRedirect('thank_you')
    else:
        form = ClientForm()

    return render(request, 'contact.html', {'form': form})

# [TODO] Develop CreateView generic view for form
from django.views.generic.edit import CreateView

class CreateShelter(CreateView):
    model = Shelter
    fields = ['shelter_name', 'shelter_location']
    template_name = "shelter_form.html"

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect('shelter_list')

# [TODO] Create ListView to add shelters to update_delete_shelters template
class ShelterEdits(ListView):
    model = Shelter
    context_object_name = 'current_shelter_list'   # your own name for the list as a template variable
    template_name = "update_delete_shelters.html"

# [TODO] Develop UpdateView and DeleteView for forms
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

class UpdateShelter(UpdateView):    
    model = Shelter
    fields = ['shelter_name', 'shelter_location']
    template_name = "update_shelter.html"

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect('/dog_shelters/update_delete_shelters')

class DeleteShelter(DeleteView):
    model = Shelter
    template_name = "delete_shelter.html"

    success_url = '/dog_shelters/update_delete_shelters'