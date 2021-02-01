[1]: https://docs.djangoproject.com/en/3.1/ref/django-admin/ "Command-line Utility"

Now that we have explored some basic concepts of Django let's begin creating the project.

## Create a project with Django-admin

Before we actually start coding there is one thing left to do in order to create a Django project. 

1. Navigate to the folder in which the virtual environment is located, and type the following in the command prompt.

    > [!NOTE] 
    > Remember to type this command in the activated virtual environment command prompt.

    ```bash
    django-admin startproject myfirstproject
    ```

After running the above command the new project should now be in your chosen directory. In this instance you would see a new folder called 'myfirstproject'.

## Navigating the project structure

Now that the Django project has been created let's look at the structure to see what was included.

```text
myfirstproject/
    manage.py
    myfirstproject/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```

- The outer **myfirstproject** in the structure is your root directory which contains the entire project.
- **manage.py**. is a command-line utility created in every Django project and actually has the same function as 'django-admin'. Below is an example of how this could be used if you were inside the project folder and wanted to see the available subcommands. 

    ```bash   
    django-admin help
   
    #OR

    python manage.py help
    ``` 

- **myfirstproject** is considered the Python package for your project.
- **init.py**, an empty file which functions to tell Python that this directory should be considered a package.
- **settings.py** contains all of your settings or configurations.
- **urls.py** contains the urls within the project.
- **asgi.py** and **wsgi.py** serve as the entry point for your web servers depending on what type of server is deployed.

For more information about the Django CLI, you can consult the [django-admin documentation][1].

## Running the project

Now that Django is installed, a project has been created, and we have examined the project structure it is time to make sure our project is working correctly.

1. Navigate to the **myfirstproject** root directory and enter the following.

    ```bash      
    python manage.py runserver
    ```

If the project runs correctly it will start to perform system checks and start your development server. Copy and paste the URL of your development server in your preferred browser and you should see a Django 'Congratulations' page with a rocket taking off.

## Hello, world!

Now that we have learned the basics about the Django framework, and examined the folder structure of our project it is time to create our first app! While this is a simple **Hello, world!** app it will give you the starting blocks in understanding how apps are created and how they work in unison with the Django project.

1. In order to create the app, we first start by navigating to the inside of the project root folder **myfirstproject** and input the following on the command line.

    ```bash    
    python manage.py startapp hello_world
    ```

With this command, Django will automatically create the required folders and files and the following structure should now be visible.

```text         
hello_world/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```        
           
## Creating a view

Now that the app structure has been created, we can begin to take the necessary steps so it will perform a simple function. The first step in the process is to create a view.  

1. Navigate to the **views.py** file contained within the **hello_world** directory and add the below code under the comment that reads `# [TODO]: Add code below to create view`.

    ```python
    # [TODO]: Add code below to create view
    from django.http import HttpResponse

    def index(request):
        return HttpResponse("Hello, world!")
    ```
        
Creating a view is an essential action as it handles what views to return when a specific URL is sent as a request. In the next section we will now map the URL to this view. 

## Create the URLconf

Now that a view has been created, the next step is to map it to the appropriate URL.
        
1. To begin this process create another file in the **hello_world** directory named **urls.py**.

    ```python
    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.index, name='index'),
    ]
    ```

The most important part of this code is the `urlpatterns` tuple, as this is where the views and URLs are connected or mapped. As you can see, we have imported our **views.py** file so we are able to use it within the `urlpatterns` line. 

Now that we have created our `URLconf` for our app, we must now create one in our project root directory.

1. Click the second **myfirstproject** folder in your project 
1. Open the **urls.py** file to enter the code under the comments `# [TODO]: Add the include function to the list of imports from django.urls` and `# [TODO]: Add the code to create the URLconf for the project`.

    ```python
    # [TODO]: Add the include function to the list of imports from django.urls
    from django.urls import include, path

    urlpatterns = [
        # [TODO]: Add the code to create the URLconf for the app
        path('hello_world/', include('hello_world.urls')),
        path('admin/', admin.site.urls),
    ]
    ```

When opening the file you will notice Django has already populated some of the code, and our task will be to add our new app path to the existing code. In addition to adding the new path, you will also need to import another function named `include` from `django.urls`. 
    
## Running your first app

Now that the structure is complete, views have been added, and the URLs mapped it is time to run your app. If you have not connected the server then navigate to the **myfirstproject** root directory and enter the below code.

    ```bash      
    python manage.py runserver
    ```

After starting the server enter the below link into your preferred browser.

    http://localhost:8000/hello_world/

If the app is functioning properly then you should see "Hello, world!" at the top left hand of the screen.