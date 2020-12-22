Now that the templates have been completed we need to add them to our **dog_shelters** app. By creating a view we will then be able to define the template that will be returned when a link is clicked, and allow for further processing of the data.

Since the **index.html** and **shelter_spotlight.html** need to be included in our app the first step is to add the below code to the **views**.**py** file.

```python
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
```

Now that we have gone over the standard way to format template views, let's look at another way to present views.

## Generic Views

### Creating list pages using generic views


### Creating detail pages using generic views


Now that we have decided how to present our template views let's move on to creating the ***URLconf*** for our app. By adding this code we are defining what will be returned when one of the links on the site is clicked. Making sure you are still in the **dog_shelter** app go to the **urls**.**py** to add the below code.

```python
# [TODO]: Add the code below to create the URLconf for the app

from django.urls import path
from . import views

urlpatterns = [
    path('home', views.index, name='index'),
    path('shelter_spotlight', views.spotlight, name='spotlight'),
]
```
After registering the paths in the app we now have to register the app paths in the project. Go to the project **mydjangoproject** and find the **urls**.**py** file to enter the below code.

```python
# [TODO]: add include to the list of imports
from django.urls import include, path

# [TODO]: Add the needed imports for the image field defined in the models
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # [TODO]: Add the below line to create the URLconf for the project
    path('dog_shelters/', include('dog_shelters.urls')),
    path('admin/', admin.site.urls),
    # [TODO]: Add the needed urlpatterns for the image upload
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

By adding the **'dog_shelters/'** path we have now connected our app to the project. Let's see what it looks like now with the new templates added. If your project isn't already running then enter **python manage**.**py runserver** to start the app, and enter the below URL in your preferred browser.

http://localhost:8000/dog_shelters/

If eveything is configured correctly you should see the home page of the site.

![Home Page](../Module4/Module4_Images/Module4_AppHomePage.PNG)

Then clink the link in the left side navigation named **Shelter Spotlight** to see the dog that is highlighted.

![Shelter Spotlight Page](../Module4/Module4_Images/Module4_AppShelterSpotlightPage.PNG)