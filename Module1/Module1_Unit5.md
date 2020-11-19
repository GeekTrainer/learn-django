## Creating Your First App

### Exercise: Hello, world!

In order to create the app, we first start by navigating to the project root folder __myfirstproject__ and input the following on the command line.
        
    python manage.py startapp hello_world
           
With this command, Django will automatically create the required folders and files and the following structure should now be visible.

          
    hello_world/
        __init__.py
        admin.py
        apps.py
        migrations/
            __init__.py
        models.py
        tests.py
        views.py
        
           
### Creating a View

Now that the app structure has been created, we can begin to take the necessary steps so it will perform a simple function. The first step in the process is to create a view.  

Navigate to the __views__.__py__ file contained within the __hello_world__ directory and enter the below information:

    from django.http import HttpResponse

    def index(request):
        return HttpResponse("Hello, world!")

        
Creating a view is an essential action as it handles what views to return when a specific URL is sent as a request. In the next section, we will now map the URL to this view. 

### URL Mapping

Now that a view has been created, the next step is to map it to the appropriate URL. In Django this is called a URLconf and it serves as a table of contents for your app.
        
To begin this process create another file in the __hello_world__ directory named __urls__.__py__ and enter the below code.

    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.index, name='index'),
    ]

The most important part of this code is the __urlpatterns__ tuple, as this is where the views and URLs are connected or mapped. As you can see, we have imported our __views__.__py__ file so we are able to use it within the __urlpatterns__ line. 

Now that we have created our URLconf for our app, we must now create one in our project root directory.

Click the second __myfirstproject__ folder in your project and open the __urls__.__py__ file to enter the below code.

    from django.contrib import admin
    from django.urls import include, path
    
    urlpatterns = [
        path('hello_world/', include('hello_world.urls')),
        path('admin/', admin.site.urls),
    ]

When opening the file you will notice Django has already populated some of the code, and our task will be to add our new app path to the existing code. In addition to adding the new path, you will also need to import another function named __include__ from __django.urls__. 

### Understanding the __Include__ Function

As you continue to learn and have more complex file structures, you will add more views and URLs for your app. Through the use of URLconfs this function plays a key role as it gives the freedom to add folders and files within a project without breaking any functionalities.

For example, we currently have the path __/hello_world/__ that directs us to our index view and displays "Hello, world!". Let's say we wanted to add another view to our app so we could display a simple greeting to the user. In order to add another view we would add the following to our __hello_world.views.py__ file.

    def user(request, user_id)
        response = "Hello user # %s."
        return HttpResponse(response % user_id)

Next in the __hello_world/url.py__ file add the following:

    path('<user_id>', views.user, name='user'),

If we now called this view by adding __/hello_world/5__ in our browser, Django would first look in __myfirstproject.urls__ and search for the urlpatterns. 

After finding the first match for __hello_world/__, it would then strip that part from the URL and continue with the remaining string to the __hello_world.urls__ where it would continue looking for a match. After finding the match, it would then diplay the appropriate view. 

This function allows a simple way to manage and organize URLs within the application and provides greater freedom to change path roots without breaking the app.

    
### Running Your First App

Now that the structure is complete, views have been added, and the URLs mapped, it is time to run your app. Make sure the server is connected and running, and enter the below link into your browser.

    http://localhost:8000/hello_world/

If the app is functioning properly then you should see "Hello, world!" at the top left hand of the screen.