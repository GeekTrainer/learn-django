## Hello, world!

In order to create the app, we first start by navigating to the inside of the project root folder **myfirstproject** and input the following on the command line.

[!NOTE] If you have decided to clone the app starting folder structure from the GitHub repository you can skip to the next step of **Creating a View**.

```bash    
python manage.py startapp hello_world
```

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
        
           
## Creating a view

Now that the app structure has been created, we can begin to take the necessary steps so it will perform a simple function. The first step in the process is to create a view.  

Navigate to the **views**.**py** file contained within the **hello_world** directory and add the below code under the comment that reads `# [TODO]: Add code below to create view`.

```python
# [TODO]: Add code below to create view
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world!")
```
        
Creating a view is an essential action as it handles what views to return when a specific URL is sent as a request. In the next section, we will now map the URL to this view. 

## URL mapping

Now that a view has been created, the next step is to map it to the appropriate URL. In Django this is called a URLconf and it serves as a table of contents for your app.
        
To begin this process create another file in the **hello_world** directory named **urls**.**py** and add the below code under the comment that reads `# [TODO]: Add the code below in the newly created file urls.py`.

```python
# [TODO]: Add the code below in the newly created file urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

The most important part of this code is the **urlpatterns** tuple, as this is where the views and URLs are connected or mapped. As you can see, we have imported our **views**.**py** file so we are able to use it within the **urlpatterns** line. 

Now that we have created our URLconf for our app, we must now create one in our project root directory.

Click the second **myfirstproject** folder in your project and open the **urls**.**py** file to enter the code under the comments `# [TODO]: Add the include function to the list of imports from django.urls` and `# [TODO]: Add the code to create the URLconf for the project`.

```python
# [TODO]: Add the include function to the list of imports from django.urls
from django.urls import include, path

urlpatterns = [
    # [TODO]: Add the code to create the URLconf for the app
    path('hello_world/', include('hello_world.urls')),
    path('admin/', admin.site.urls),
]
```

When opening the file you will notice Django has already populated some of the code, and our task will be to add our new app path to the existing code. In addition to adding the new path, you will also need to import another function named **include** from **django.urls**. 

## Understanding the **include** function

As you continue to learn and have more complex file structures, you will add more views and URLs for your app. Through the use of URLconfs this function plays a key role as it gives the freedom to add folders and files within a project without breaking any functionalities.

For example, we currently have the path **/hello_world/** that directs us to our index view and displays "Hello, world!" on the screen. Let's say we wanted to add another view to our app so we could display a simple greeting to the user. In order to add another view we would add the following to our **hello_world/views.py** file.

```python
def user(request, user_id)
    response = "Hello user # %s."
    return HttpResponse(response % user_id)
```

After adding the view we would then add the following to the **hello_world/url.py** file.

```python
path('<user_id>', views.user, name='user'),
```

Now let's say we called a user number in the URL.

    http://localhost:8000/hello_world/5

Django would first look in **myfirstproject.urls** and search for the urlpatterns. After finding the first match for **hello_world/**, it would then strip that part from the URL just leaving **5**. It would then continue with the remaining string to the **hello_world/urls.py** file where it would continue looking for a match. After finding the match, it would then diplay the appropriate view.

    Hello user # 5.

By using this function it allows for a simple way to manage and organize URLs within the application and provides greater freedom to change path roots without breaking the app.

    
## Deploying your first app

Now that the structure is complete, views have been added, and the URLs mapped it is time to run your app. If you have not connected the server then navigate to the **myfirstproject** root directory and enter the below code.

```bash      
python manage.py runserver
```
After starting the server enter the below link into your preferred browser.

    http://localhost:8000/hello_world/

If the app is functioning properly then you should see "Hello, world!" at the top left hand of the screen.