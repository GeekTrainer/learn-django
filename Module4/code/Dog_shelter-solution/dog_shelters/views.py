from django.shortcuts import render

# [TODO] Create your views
from dog_shelters.models import Shelter, Dog

def index(request):

    # Generate count of dog shelters in database
    num_shelters = Shelter.objects.all().count()

    # Generate count of dogs ready for adoption in database
    num_dogs = Dog.objects.all().count()

    return render(request, 'index.html', {'num_shelters': num_shelters, 'num_dogs': num_dogs})

def spotlight(request):

    # Generate count of dog shelters in database
    get_shelters = Shelter.objects.all()

    # Generate count of dogs ready for adoption in database
    get_dogs = Dog.objects.all()

    return render(request, 'shelter_spotlight.html', {'get_shelters': get_shelters, 'get_dogs': get_dogs})